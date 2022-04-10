from threading import Thread
from pygame import mixer
import pyvirtualcam
import cv2
import moviepy.editor as mp
from pathlib import Path
from video.listen import main


def split_mp4(video_path: str, audio_path: str):
    clip = mp.VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)
    

def play_music(path: str):
    mixer.init(devicename=None)
    mixer.music.load(path)
    mixer.music.play()

        
def play_video(frames):
    with pyvirtualcam.Camera(width=1280, height=720, fps=25) as cam:
        for frame in frames:
            cam.send(frame)
            cam.sleep_until_next_frame()


def play_music(file_path):
    print(file_path)
    mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
    mixer.music.load(file_path)
    mixer.music.play()
    

def get_frames(path: str):
    frames = []
    cap = cv2.VideoCapture(path)
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frames.append(frame)
        if cv2.waitKey(1) == ord('q'):
            break
        
    return frames

if __name__ == "__main__":
    VIDEO_PATH = Path("/Users/ryandowning/Downloads/result_voice.mp4")
    AUDIO_PATH = VIDEO_PATH.parents[0] / f"{VIDEO_PATH.stem}.mp3"
    if not AUDIO_PATH.exists():
        split_mp4(VIDEO_PATH, AUDIO_PATH)
    VIDEO_PATH = str(VIDEO_PATH)
    AUDIO_PATH = str(AUDIO_PATH)
    
    frames = get_frames(VIDEO_PATH)
    
    def on_name():
        Thread(target=play_music, args=(AUDIO_PATH,)).start()
        Thread(target=play_video, args=(frames,)).start()
        
    print("Beginning transcriptions")
    main(on_name, "Peter")
