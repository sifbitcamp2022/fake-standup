import numpy as np
import time
import pyvirtualcam
from pygame import mixer

mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')


def generate_rgb_noise(dim: tuple) -> np.ndarray:
    return (np.random.random(dim) * 256).astype(np.uint8)


def play_video():
    with pyvirtualcam.Camera(width=1280, height=720, fps=5) as cam:
        frame = np.zeros((cam.height, cam.width, 3), np.uint8)  # RGB
        while True:
            cam.send(generate_rgb_noise((cam.height, cam.width, 3)))
            cam.sleep_until_next_frame()


def play_music(count=1):
    mixer.music.load("C:\\Users\\iwann\\Downloads\\sixflags.mp3")
    mixer.music.play()
    time.sleep(14)
    if count == 10:
        return
    play_music(count + 1)
