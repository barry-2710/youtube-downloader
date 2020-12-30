from kivy.app import App
from kivymd.theming import ThemeManager
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.toast import toast
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock, mainthread
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.menu import MDDropdownMenu
import dmp3 as dm
import dmp4 as dm4
import time
import threading
import time
from pytube import YouTube
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage 
from kivymd.uix.snackbar import Snackbar
import writehistory as wh
import show_history as sh
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.picker import MDThemePicker

class MyLayout(BoxLayout):

    stop = threading.Event()
    scr_mngr = ObjectProperty(None)
    dropdown = ObjectProperty()
    
    
    def go_on(self):
        self.scr_mngr.screen1.proceed_mp3.disabled=True
        url = self.scr_mngr.screen1.audio_url.text
        print(url)
        toast("Starting to download")
        threading.Thread(target=self.download, args=(url,)).start()
        
    def verify(self):
        print(self)
        
        url = self.scr_mngr.screen1.audio_url.text

        if(url==""):
                toast("Please fill the URL")
        else:
            
            threading.Thread(target=self.after_url, args=(url,)).start()

    def after_url(self,url):
        try:
            yt = YouTube(url)
            title = yt.title
            name1 = ""
            for elem in title:
                if(elem=='|'):
                    break
                else:
                    name1 += elem
            #return Image(source ='download.jpg')
            self.scr_mngr.screen1.song_name_mp3.text=name1
            
            self.scr_mngr.screen1.thumbnail_mp3.source=yt.thumbnail_url
            
            self.scr_mngr.screen1.proceed_mp3.add_widget(
                MDLabel(
                    id="blank",
                    text="                   ",
                    halign="center",
                    pos_hint ={'x':.2, 'y':-.3}

                )
            )
            self.scr_mngr.screen1.proceed_mp3.disabled=False
            

                                
        except Exception as e:
            toast("Error")
            print(e)
    
    def download(self,url):
        start = time.time()
        dm.download_mp3(url)
        end = time.time()
        toast("Downloaded")
        print("Downloaded")
        print("Time taken",end-start)
        wh.write_history(url,"mp3")

    def test(self):
        self.scr_mngr.current='screen2'
        download_list = sh.show()
        download_list.pop(0)
        for elem in download_list:
            self.scr_mngr.screen2.container.add_widget(
                TwoLineListItem(text=(str(elem[0]))+") "+elem[1],secondary_text=(elem[2]+" / "+elem[3]))
            )
    def test1(self):
        self.scr_mngr.current='screen1'
        self.clear_screen()

    def clear_screen(self):
       self.scr_mngr.screen2.container.clear_widgets()

   ###########################################################################downloadMP4##################################

    def download_mp4(self):
        
        url = self.scr_mngr.screen1.video_url.text
        if(url==""):
            toast("Please enter the URL")
        else:
            

            threading.Thread(target=self.thread_mp4, args=(url,)).start()
            
    def thread_mp4(self,url):
        try:
            yt = YouTube(url)
            title = yt.title
            name1 = ""
            for elem in title:
                if(elem=='|'):
                    break
                else:
                    name1 += elem


            self.scr_mngr.screen1.song_name_mp4.text=name1
            
            self.scr_mngr.screen1.thumbnail_mp4.source=yt.thumbnail_url
            self.scr_mngr.screen1.proceed_mp4.disabled=False
        except Exception as e:
            toast("Error")

    def res(self):
        
        url = self.scr_mngr.screen1.video_url.text
        
        val = self.res_continue(url)
        return val

        

    def res_continue(self,url):
        yt = YouTube(url)
        l=[]
        def callback_for_menu_items(text_of_the_option):
            toast("Starting to download")
            threading.Thread(target=self.continue_download_mp4, args=(text_of_the_option,)).start()
        l = []
        g=[]
        menu_labels = []

        for i in yt.streams.filter(subtype='mp4').order_by('resolution').desc(): l+=[i.resolution]

        l = list(dict.fromkeys(l))
        for elem in l:
            if(elem=='1080p'):
                l.remove('1080p')
        for i in l:
            menu_labels += [
                        {"viewclass": "MDMenuItem",
                            "text": i,
                            "callback": callback_for_menu_items},]
        for i in yt.streams.filter(progressive=True).order_by('resolution').desc(): g+=[i.resolution]
        for i in g:
            menu_labels += [
                        {"viewclass": "MDMenuItem",
                            "text": i+"(Fast Download)",
                            "callback": callback_for_menu_items},]
        return(menu_labels)

    def continue_download_mp4(self,option):
        url = self.scr_mngr.screen1.video_url.text
        yt = YouTube(url)
        l = ["144p(Fast Download)","240p(Fast Download)","360p(Fast Download)","480p(Fast Download)","720p(Fast Download)"]
        if(option in l):
            yt.streams.filter(progressive=True).first().download('F:\Bharath_projects\python\YouDownloadComplete\downloads')
            toast("Downloaded")
            wh.write_history(url,"mp4")
        else:
            dm4.download_mp4(option,yt)
            wh.write_history(url,"mp4")
    def barry(self):
        toast("Thank you, for using the App")
            
    

   

        

class MainApp(App):
    title = "YouDownload"
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'Purple'
    theme_cls.accent_palette = 'LightBlue'
    theme_cls.theme_style = 'Light'  
    def on_stop(self):
        # The Kivy event loop is about to stop, set a stop signal;
        # otherwise the app window will close, but the Python process will
        # keep running until all secondary threads exit.
        self.root.stop.set()
    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()
    
    
         

if __name__ == "__main__":
	  MainApp().run()