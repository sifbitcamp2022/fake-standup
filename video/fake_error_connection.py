import numpy as np
import time
import ffmpeg
import pyvirtualcam
from pygame import mixer
import moviepy.editor as mp

mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')


def generate_rgb_noise(dim: tuple) -> np.ndarray:
    return (np.random.random(dim) * 256).astype(np.uint8)

def video_to_frames(path: str) -> np.ndarray:
    out, _ = (
    ffmpeg
    .input(path)
    .output('pipe:', format='rawvideo', pix_fmt='rgb24', vframes=900)
    .run(capture_stdout=True)
    )
    video = (
        np
        .frombuffer(out, np.uint8)
        .reshape([-1, 720, 1280, 3])
    )
    return video


def play_video(queue):
    with pyvirtualcam.Camera(width=1280, height=720, fps=25) as cam:
        frame = generate_rgb_noise((cam.height, cam.width, 3))
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
