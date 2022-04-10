import numpy as np
import time
import pyvirtualcam
from pygame import mixer
import moviepy.editor as mp

mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')


def generate_rgb_noise(dim: tuple) -> np.ndarray:
    return (np.random.random(dim) * 256).astype(np.uint8)


def play_video(queue):
    with pyvirtualcam.Camera(width=320, height=240, fps=25) as cam:
        while True:
            if not queue.empty():
                frame = queue.get()
            cam.send(frame)
            cam.sleep_until_next_frame()


def play_music(queue):
    while True:
        if not queue.empty():
            file_path = queue.get()
            mixer.music.load(file_path)
            mixer.music.play()

def write_audio(video_path: str, audio_path: str):
    clip = mp.VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)
