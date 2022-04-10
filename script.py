from threading import Thread
from video.fake_error_connection import play_video, play_music, video_to_frames
from video.listen import main


def coordinate(audio_file, frames):
    Thread(target=play_music, args=(audio_file,)).start()
    Thread(target=play_video, args=(frames,)).start()


if __name__ == "__main__":
    video_file = "result_voice.mp4"
    audio_file = "result_audio.mp3"
    frames = video_to_frames(video_file)
    print("Frames processing done!")


    def on_name():
        coordinate(audio_file, frames)
    print("Beginning transcription.")
    main(on_name, "Ryan")

