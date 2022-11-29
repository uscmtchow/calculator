# 11/29/2022
# Created by Max Chow

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
    def __init__(self, **var_args):
        super(LoginScreen, self).__init__(**var_args)

        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        # password true is used to hide it
        # by * self.add_widget(self.password)
        self.add_widget(Label(text='Comfirm password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


# the Base Class of our Kivy App
class MyApp(App):
    def build(self):
        # return a LoginScreen() as a root widget
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()