from kivy.app import App
from kivymd.theming import ThemeManager
from pytube import YouTube
import time


class TestApp(App):
    title = "KivyMD MDDropdownMenu Demo"
    theme_cls = ThemeManager()
    menu_labels = []
    
    url = "https://www.youtube.com/watch?v=1zRe8UPF1tM"
    
    def test(self):
        try:
        
            yt = YouTube(self.url)
            l=[]
            menu_labels = []
            def callback_for_menu_items(text_of_the_option):
                print(text_of_the_option)
            l = []
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
            return(menu_labels)
        except Exception as e:
            print("error")
    
    
    

t = TestApp()  
if __name__ == "__main__":
    TestApp().run()    