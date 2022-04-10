from threading import Thread
from video.fake_error_connection import play_video, play_music, video_to_frames, generate_rgb_noise


def coordinate():
    print("coordinate")
    video_file = "result_voice.mp4"
    audio_file = "result_audio.mp3"
    frames = video_to_frames(video_file)
    # frames = [generate_rgb_noise((720, 1280, 3)) for i in range(100)]
    print("Frames processing done!")
    Thread(target=play_music, args=(audio_file,)).start()
    Thread(target=play_video, args=(frames,)).start()

    # video_queue = Queue()
    # p2 = Process(target=play_video, args=(video_queue,))
    # p2.start()

    # while True:
    #     if not queue.empty():
    #         r = queue.get()
    #         music_queue.put(audio_file)
    #         # for frame in frames:
    #         #     video_queue.put(frame)
    #         break


if __name__ == "__main__":
    coordinate()
