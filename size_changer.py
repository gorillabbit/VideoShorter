import ffmpeg
import glob
import os

der = __file__[:-15]
print(der)
videos = glob.glob(der+"*.mp4")

for video in videos:
    print(video)
    basename = os.path.splitext(os.path.basename(video))[0]
    ffmpeg.input(video).output("H:/videos/output/" + basename+".mp4", r=15, s='1280x720', video_bitrate='1200k', audio_bitrate='8000k').run()
