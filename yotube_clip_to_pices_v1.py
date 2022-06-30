'''

- downloads an hour-long lecture about Socrates (The Ancients: Socrates)

- saves it as mp3 on your computer

- then chops the mp3 to 10 minutes long files with 3s overlaps

- the files are saved in a new directory 

'''

from pytube import YouTube
from moviepy.editor import *

import os, shutil

# ## Code to download MP3
yt = YouTube('https://www.youtube.com/watch?v=c6OtjYz3WY8')

video = yt.streams.filter(only_audio=True).first()

out_file = video.download(output_path="")

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

file = base + new_file


# # ## Code to cut the file 
file_name = base.split('\\')[-1] + '.mp3'

path_out = os.path.join(os.getcwd(), file_name[:-4])
if os.path.isdir(path_out):
    print('Deleting the old output directory. ')
    shutil.rmtree(path_out)
print('Creating a new output direcory.')
os.makedirs(path_out)

print(  os.path.join(os.getcwd(), file_name)  )

# loading video dsa gfg intro video 
clip = AudioFileClip(os.path.join(os.getcwd(), file_name)) 

duration = clip.duration # get mp3 duration

end = clip.duration
timer = 0
counter = 1
loopa = True
buffor = 3  # overlap seconds
chunk = 600  # length of the episode in seconds

while loopa:
    mp3_name = f'ep_{counter}.mp3'
    start = timer

    counter += 1
    timer += chunk

    if timer + chunk >= end:
        print(f"{mp3_name} Start: {start - buffor} End: {end}")
        episod = clip.subclip(start - buffor, end)

        episod.write_audiofile(os.path.join(path_out, mp3_name))
        break

    if counter == 2:
        print(f"{mp3_name} Start: {start} End: {timer}")
        episod = clip.subclip(start, timer)

        episod.write_audiofile(os.path.join(path_out, mp3_name))
    else:
        print(f"{mp3_name} Start: {start - buffor} End: {timer}")
        episod = clip.subclip(start - buffor, timer)

        episod.write_audiofile(os.path.join(path_out, mp3_name))

