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
    def update(*kwargs, self, new):
        self.ids.lineWatcher.text = new
        # print(self.ids.lineWatcher.text)


class fakeRoot(Screen):
    pass


class WaitLineVisual(GridLayout):
    pass
    # def show_labels(self, strings):
    #     self.clear_widgets()

    #     for text in strings:
    #         label = Label(text=text)
    #         self.add_widget(label)

    # def update(*kwargs, self, new):
    #     print(self.ids.values)
    # self.ids.lineWatcher.text = new


class LineWatcherLabel(Label):
    # def update(self, *args, new):
    #     self.text = new
    def update(self, new):
        self.text = new
