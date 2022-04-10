from multiprocessing import Process, Queue
import cv2
from video.fake_error_connection import play_video, play_music, write_audio


def coordinate(queue):
    music_queue = Queue()
    p1 = Process(target=play_music, args=(music_queue,))
    p1.start()

    video_queue = Queue()
    p2 = Process(target=play_video, args=(video_queue,))
    p2.start()

    while True:
        if not queue.is_empty():
            queue.get()
            video_file = "result_voice.mp4"
            audio_file = "result_audio.mp3"
            vidcap = cv2.VideoCapture(video_file)
            success, image = vidcap.read()
            music_queue.put(audio_file)
            while success:
                video_queue.put(image)
                success, image = vidcap.read()


if __name__ == "__main__":
    q = Queue()
    p = Process(target=coordinate, args=(q,))
    p.start()

    input()
    q.put("Hello")
