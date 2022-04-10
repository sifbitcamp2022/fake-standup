from multiprocessing import Process, Queue
from video.fake_error_connection import play_video, play_music, video_to_frames


def coordinate(queue):
    video_file = "result_voice.mp4"
    audio_file = "result_audio.mp3"
    frames = video_to_frames(video_file)
    print("Frames processing done!")
    music_queue = Queue()
    p1 = Process(target=play_music, args=(music_queue,))
    p1.start()

    video_queue = Queue()
    p2 = Process(target=play_video, args=(video_queue,))
    p2.start()

    while True:
        if not queue.is_empty():
            queue.get()
            music_queue.put(audio_file)
            for frame in frames:
                video_queue.put(frame)


if __name__ == "__main__":
    q = Queue()
    p = Process(target=coordinate, args=(q,))
    p.start()

    input()
    q.put("Hello")
