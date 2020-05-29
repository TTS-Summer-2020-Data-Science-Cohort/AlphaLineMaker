import plyer
import json
import requests
import kivy
from functools import partial
from kivy.app import App
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.core.window import Window
from kivy.core.image import Image as CoreImage
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.modules import inspector
from kivy.clock import Clock
from uiDeclarations import LandingScreenWrapper, LandingScreen, InLineScreen, MakeLineScreen, ManageLineScreen, ManageWaitScreen, ScreenChanger, root, WaitLineVisual, LineWatcherLabel
from fireBaseConfig import webAPIKey, authKey, baseUrl

kivy.require('2.0.0')
Window.size = (320, 420)

kv = Builder.load_file("mylinemaker.kv")


class MyLineMaker(App):
    # find unique id for each user using plyer based on device
    # deviceId = plyer.uniqueid.id
    deviceId = "A literal cat"
    img = CoreImage("person.png")
    currentQueue = ''
    placeInQueueId = ''
    placeInQueue = 'What'
    managedQueue = False

    def getFirebaseUrl(self, key):
        urlSuffix = '.json'
        return baseUrl + key + urlSuffix + '?auth=' + authKey

    def joinQueue(self, queueToJoin):
        if(queueToJoin in self.allQueues):
            self.currentQueue = queueToJoin
            response = requests.post(
                self.getFirebaseUrl(queueToJoin), json="")
            self.placeInQueueId = json.loads(response.content)['name']
            print(self.placeInQueueId)
        else:
            print("That is not a valid line")

    def leaveQueue(self):
        if(self.currentQueue != ''):
            requests.delete(self.getFirebaseUrl(
                self.currentQueue + "/" + self.placeInQueueId))
            self.currentQueue = ''

    def createQueue(self, queueToCreate):
        # Error for getting empty queues that is not able to be iterated :(
        if(queueToCreate in self.allQueues):
            print(f'Managing line for {queueToCreate}')
        else:
            requests.patch(self.getFirebaseUrl(""), json=json.loads(
                '{"' + queueToCreate + '": {"End of line": " "}}'))
            self.managedQueue = queueToCreate

    def destroyQueue(self, queueToDestroy):
        if(self.managedQueue == True):
            requests.delete(self.getFirebaseUrl(
                queueToDestroy))
            self.managedQueue = False
        else:
            print("This would've deleted all entries")

    # def getQueue(self):
    #     response = requests.get(self.getFirebaseUrl(self.currentQueue))
    #     queue = json.loads(response.content)
    #     placeInQueue = list(queue.keys()).index(self.placeInQueueId) + 1
        # for i in queue:
        #     if(i != 'End of line'):
        #         WaitLineVisual.add_widget((Image=self.img))
        # WaitLineVisual.add_widget((Label(text=placeInQueue)))

    def getPlace(self, *kwargs):
        if(self.currentQueue != ''):
            response = requests.get(self.getFirebaseUrl(self.currentQueue))
            queue = json.loads(response.content)
            self.placeInQueue = list(queue.keys()).index(
                self.placeInQueueId) + 1
            print(self.placeInQueue)
        else:
            self.placeInQueue = 'Not in line yet'

    def getAllQueues(self, *kwargs):
        response = requests.get(self.getFirebaseUrl(""))
        self.allQueues = json.loads(response.content)
        print(self.allQueues)

    def getManagedQueue(self):
        response = requests.get(self.getFirebaseUrl(self.managedQueue))
        queue = json.loads(response.content)
        print(queue)

    def acceptNextInQueue(self):
        if(self.managedQueue == True):
            foundQueue = map(
                lambda i: i == self.managedQueue, self.allQueues)
            print(foundQueue)
        print(self.managedQueue)

    def anim(self, widge, xDest, yDest):
        anim = Animation(x=xDest, y=yDest, duration=2.)
        anim.start(widge)

    # Build the kv file

    def build(self):
        inspector.create_inspector(Window, ScreenChanger)
        sc = ScreenChanger()
        lw = sc.ids.lineWatcher
        self.getAllQueues()
        Clock.schedule_interval(self.getAllQueues, 20)
        Clock.schedule_interval(self.getPlace, 20)
        Clock.schedule_interval(partial(lw.update, new=self.placeInQueue), 20)
        return kv


if __name__ == '__main__':
    MyLineMaker().run()
