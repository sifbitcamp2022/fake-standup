import argparse
import os
from pathlib import Path

import librosa
import numpy as np
import soundfile as sf
import torch

from encoder import inference as encoder
from encoder.params_model import model_embedding_size as speaker_embedding_size
from synthesizer.inference import Synthesizer
from utils.argutils import print_args
from utils.default_models import ensure_default_models
from vocoder import inference as vocoder



ENC_PATH = Path("saved_models/default/encoder.pt")
SYN_PATH = Path("saved_models/default/synthesizer.pt")
VOC_PATH = Path("saved_models/default/vocoder.pt")

class TextToSpeech:
    def __init__(self, reference_path: str) -> None:
        print("Running a test of your configuration...\n")
        ## Load the models one by one.
        print("Preparing the encoder, the synthesizer and the vocoder...")
        ensure_default_models(Path("saved_models"))
        encoder.load_model(ENC_PATH)
        self.synthesizer = Synthesizer(SYN_PATH)
        vocoder.load_model(VOC_PATH)
        # message = "Reference voice: enter an audio filepath of a voice to be cloned (mp3, " \
        #                 "wav, m4a, flac, ...):\n"
        in_fpath = Path(reference_path)

        ## Computing the embedding
        # First, we load the wav using the function that the speaker encoder provides. This is
        # important: there is preprocessing that must be applied.

        # The following two methods are equivalent:
        # - Directly load from the filepath:
        preprocessed_wav = encoder.preprocess_wav(in_fpath)
        # - If the wav is already loaded:
        original_wav, sampling_rate = librosa.load(str(in_fpath))
        preprocessed_wav = encoder.preprocess_wav(original_wav, sampling_rate)
        print("Loaded file succesfully")

        # Then we derive the embedding. There are many functions and parameters that the
        # speaker encoder interfaces. These are mostly for in-depth research. You will typically
        # only use this function (with its default parameters):
        embed = encoder.embed_utterance(preprocessed_wav)
        self.embeds = [embed]
        print("Created the embedding")

    def generate_speech(self, sentence: str, save_file_path: str) -> None:
        # save_file_path includes file extension
            # Get the reference audio filepath
                            ## Generating the spectrogram
            # text = input("Write a sentence (+-20 words) to be synthesized:\n")

            # The synthesizer works in batch, so you need to put your data in a list or numpy array
            texts = [sentence]
            # embeds = [embed]
            # If you know what the attention layer alignments are, you can retrieve them here by
            # passing return_alignments=True
            specs = self.synthesizer.synthesize_spectrograms(texts, self.embeds)
            spec = specs[0]
            print("Created the mel spectrogram")


            ## Generating the waveform
            print("Synthesizing the waveform:")

            # Synthesizing the waveform is fairly straightforward. Remember that the longer the
            # spectrogram, the more time-efficient the vocoder.
            generated_wav = vocoder.infer_waveform(spec)


            ## Post-generation
            # There's a bug with sounddevice that makes the audio cut one second earlier, so we
            # pad it.
            generated_wav = np.pad(generated_wav, (0, self.synthesizer.sample_rate), mode="constant")

            # Trim excess silences to compensate for gaps in spectrograms (issue #53)
            generated_wav = encoder.preprocess_wav(generated_wav)
            # Save it on the disk
            filename = save_file_path
            # filename = "demo_output_%02d.wav" % num_generated
            print(generated_wav.dtype)
            sf.write(filename, generated_wav.astype(np.float32), self.synthesizer.sample_rate)
            # num_generated += 1
            print("\nSaved output as %s\n\n" % filename)

if __name__ == "__main__":
    tts = TextToSpeech("obama.mp3")
    tts.generate_speech("Hello this is you president.", "theone.wav")
