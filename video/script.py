from multiprocessing import Process
from video.fake_error_connection import play_video, play_music

if __name__ == "__main__":
    p1 = Process(target=play_music)
    p1.start()

    p2 = Process(target=play_video)
    p2.start()
