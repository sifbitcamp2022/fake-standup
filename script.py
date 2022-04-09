from multiprocessing import Process, Queue
from video.fake_error_connection import play_video, play_music

if __name__ == "__main__":
    p1 = Process(target=play_music)
    p1.start()

    video_queue = Queue()
    p2 = Process(target=play_video, args=(video_queue,))
    p2.start()

    while True:
        i = input()
        video_queue.put(1)
