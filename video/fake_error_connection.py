import numpy as np
import time
import pyvirtualcam
from pygame import mixer

mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')


def generate_rgb_noise(dim: tuple) -> np.ndarray:
    return (np.random.random(dim) * 256).astype(np.uint8)


def play_video(queue):
    with pyvirtualcam.Camera(width=320, height=240, fps=25) as cam:
        frame = generate_rgb_noise((cam.height, cam.width, 3))
        while True:
            if not queue.empty():
                frame = queue.get()
                # frame = generate_rgb_noise((cam.height, cam.width, 3))
            cam.send(frame)
            cam.sleep_until_next_frame()


def play_music(file_path, count=1):
    mixer.music.load(file_path)
    mixer.music.play()
    time.sleep(14)
    if count == 10:
        return
    play_music(count + 1)
