from ftplib import MAXLINE
from pydub import AudioSegment

import os

from voice.tts import TextToSpeech


def make_speech(text_path: str, voice_sample: str, out_file: str) -> None:
    tts = TextToSpeech(voice_sample)
    max_line = 0
    with open(text_path, 'r') as f:
        for line in f:
            line = line.strip()
            tts.generate_speech(line, os.path.join("speech_files", f"temp{max_line}.wav"))
            max_line += 1
    if max_line == 0:
        raise Exception
    
    sound = AudioSegment.from_file(os.path.join("speech_files", "temp0.wav"))

    for i in range(1, max_line):
        new_sound = AudioSegment.from_file(os.path.join("speech_files", f"temp{i}.wav"))
        sound += new_sound
    
    sound.export(out_file)


if __name__ == "__main__":
    make_speech("speech_files/text.txt", "voice/obama.mp3", "niceone.wav")
