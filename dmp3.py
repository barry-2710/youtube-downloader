from pytube import YouTube
from moviepy.editor import *
from kivymd.toast import toast
import shutil
import time
import re


def change_name(title):
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
    line +="(mp3)"
    shutil.copy2('temp.mp3', 'downloads/'+line+'.mp3')
    
    

def convert_to_mp3(title):
    print("reached mp3")
    video = VideoFileClip(os.path.join("","","temp.mp4"))
    video.audio.write_audiofile(os.path.join("","","temp.mp3"))
    change_name(title)


def convert_to_mp4(title):
    print("reached mp4")
    videoclip = VideoFileClip("resource/test.mp4")
    audioclip = AudioFileClip("temp.webm")
    output = 'temp.mp4'
    final_clip = videoclip.set_audio(audioclip)
    final_clip.write_videofile(output,threads=4,logger=None)
    videoclip.close()
    audioclip.close()
    convert_to_mp3(title)
    toast("Processing audio")



def download_mp3(url):
    print("Entered download")
    try:
        yt = YouTube(url)
        yt.streams.filter(mime_type="audio/webm").first().download(filename='temp')
        yt.register_on_complete_callback(convert_to_mp4(yt.title))
        print("fetched")
        
        
        
    except Exception as e:
        print("error",e)
        toast("Error, try again")
