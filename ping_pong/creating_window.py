# create the app
# create the game
# build the game
# run the game

from kivy.app import App
from kivy.uix.widget import Widget


class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        return PongGame()


PongApp().run()
