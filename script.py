from multiprocessing import Process, Queue
import cv2
from video.fake_error_connection import play_video, play_music

if __name__ == "__main__":
    # p1 = Process(target=play_music)
    # p1.start()

    video_queue = Queue()
    p2 = Process(target=play_video, args=(video_queue,))
    p2.start()

    vidcap = cv2.VideoCapture('C:\\Users\\iwann\\Downloads\\sample-mp4-file.mp4')
    success, image = vidcap.read()
    i = 0
    while i < 100:
        i += 1
        video_queue.put(image)
        success, image = vidcap.read()
