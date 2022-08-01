import ffmpeg
import glob
import os
src_files_v = glob.glob("H:/videos/output/concat/*.mp4")
filenames = []
txt_path = 'H:/videos/output/concat/aaa.txt'
f = open(txt_path, 'w')
for file in src_files_v:
    name = os.path.basename(file)
    filenames.append(name)
    f.write('file ' + name +'\n')
f.close()
print(filenames)
ffmpeg.input(txt_path, f='concat', safe=0).output("H:/videos/output/" + name, r=15, s='1280x720', video_bitrate='1200k', audio_bitrate='8000k').run()