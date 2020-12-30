from moviepy.editor import *
from kivymd.toast import toast
import shutil
import time
import re

def convert_to_mp4(title,option):
    print("reached mp4")
    toast("Downloaded, Processing video")
    videoclip = VideoFileClip("temp_mp4_video.mp4")
    audioclip = AudioFileClip("temp_mp4_music.webm")
    name1 = ""
    j=0
    count=0
    for elem in str(title):
        j+=1
        if(j==30):
            break
        else:
            name1 += elem
    line = str(name1)
    line = re.sub('[|]', '', line)
    
    title1 = line+"("+option+")"+".mp4"
    output = 'downloads/'+title1
    final_clip = videoclip.set_audio(audioclip)
    final_clip.write_videofile(output,threads=4,logger=None)
    videoclip.close()
    audioclip.close()
    toast("downloaded")


def download_mp4(option,yt):
    print(option,yt)
    start = time.time()
       
        
    #yt.streams.filter(resolution=option).first().download('F:\Bharath projects\python\youtube.v1\YouDownload\downloads')
    yt.streams.filter(resolution=option).first().download(filename='temp_mp4_video')
    yt.streams.filter(mime_type="audio/webm").first().download(filename='temp_mp4_music')
    yt.register_on_complete_callback(convert_to_mp4(yt.title,option))
    end = time.time()
    print("downloaded",((end-start)/60))