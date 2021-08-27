from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json
import random
from datetime import datetime
import difflib
from difflib import get_close_matches


Builder.load_file('design.kv')

class LoginScreen(Screen):
    def login(self, uname, pas):
        users = json.load(open("user.json"))
        if uname in users.keys() and users[uname]['password'] == pas:
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text = "Wrong username or password!"

    def sign_up(self):
        self.manager.current = "sign_up_screen"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self, uname, pas, mail):
        users = json.load(open("user.json"))
        users[uname] = {'username': uname,'password': pas, 'email': mail, 'created': datetime.now().strftime("%Y-%m-%d %M-%M-%S")}

        with open("user.json",'w') as file:
            json.dump(users,file)

        self.manager.current = "sign_up_screen_success"

class ImageButton(ButtonBehavior,Image,HoverBehavior):
    pass

class SignUpSuccessScreen(Screen):
    def log_in(self):
        self.manager.current = "login_screen"

class LoginSuccessScreen(Screen):
    def log_out(self):
        self.manager.current = "login_screen"

    def meme_generator(self, mood):
        moods_memes = json.load(open("moods.json"))
        mood = mood.lower()
        self.ids.meme_image.opacity = 1
        if mood in moods_memes.keys():
            meme = random.choice(moods_memes[mood]['memes'])
            self.ids.meme_image.source = "memes/" + meme

        elif len(get_close_matches(mood,moods_memes.keys(),cutoff=0.7)) > 0 :
            meme = random.choice((get_close_matches(mood,moods_memes.keys(),cutoff=0.7)))
            if(type(meme) is list):
                meme2 = meme[0]
                self.ids.meme_image.source = "memes/" + meme2
            else:
                self.ids.meme_image.source = "memes/" + meme

        else:
            self.ids.meme_image.source = "memes/fail.jpeg"
         
class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()