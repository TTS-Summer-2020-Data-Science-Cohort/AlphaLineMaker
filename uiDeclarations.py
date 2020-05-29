from kivy.uix.carousel import Carousel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class LandingScreenWrapper(Screen):
    pass


class LandingScreen(Carousel):
    pass


class InLineScreen(GridLayout):
    pass


class MakeLineScreen(GridLayout):
    pass


class ManageLineScreen(Screen):
    pass


class ManageWaitScreen(Screen):
    pass


class ScreenChanger(ScreenManager):
    pass


class root(Screen):
    pass


class WaitLineVisual(GridLayout):
    def show_labels(self, strings):
        self.clear_widgets()

        for text in strings:
            label = Label(text=text)
            self.add_widget(label)


class LineWatcherLabel(Label):
    def update(self, *args, new):
        self.text = new
