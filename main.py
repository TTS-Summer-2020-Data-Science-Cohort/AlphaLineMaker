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
from uiDeclarations import LandingScreenWrapper, LandingScreen, InLineScreen, MakeLineScreen, ManageLineScreen, ManageWaitScreen, ScreenChanger, WaitLineVisual, LineWatcherLabel, fakeRoot
# You must create your own fireBaseConfig.py file in the following format:
# authKey = <AUTH KEY>
# webAPIKey = <API KEY IF USED>
# baseUrl = 'https://<NAME OF FIREBASE DATABASE>.firebaseio.com/'
from fireBaseConfig import webAPIKey, authKey, baseUrl

kivy.require('2.0.0')
Window.size = (320, 420)

# kv = Builder.load_file("mylinemaker.kv")


class MyLineMakerApp(App):
    # find unique id for each user using plyer based on device
    # deviceId = plyer.uniqueid.id
    deviceId = "Mock ID"
    img = CoreImage("person.png")
    currentQueue = ''
    placeInQueueId = ''
    placeInQueue = 'Not in line yet'
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
        # Error for getting empty queues that is not able to be iterated
        if(queueToCreate in self.allQueues):
            print(f'Managing line for {queueToCreate}')
            self.managedQueue = queueToCreate
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
            print(str(self.placeInQueue) + "Well done")
        else:
            self.placeInQueue = 'Not'
            print(self.placeInQueue)

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

    def getPlaceInQueue(self):
        return str(self.placeInQueue)

    # Build the kv file

    def build(self):
        # inspector.create_inspector(Window, ScreenChanger)
        # sc = ScreenChanger()
        # lw = sc.ids.lineWatcher
        # kv.ids.lineWatcher.update

        self.getAllQueues()
        Clock.schedule_interval(self.getAllQueues, 20)
        Clock.schedule_interval(self.getPlace, 20)
        # CURRENT ISSUES: Why is only the initial value passed to the partial function? So the ui is only updated with the first value and nothing from the database
        # Structure of kv file is messy, what is the purpose of fakeRoot? Why can't we just use the markup in the second half of the kv file
        # How can we get the current instance variables from self and pass them to the partial function? We are probably just passing class values and not instance variables.
        Clock.schedule_interval(
            partial(self.root.ids.screenChanger.update, self=self.root.ids.screenChanger, new=self.getPlaceInQueue), 20)
        # Clock.schedule_interval(
        #     lambda WaitLineVisual: WaitLineVisual.update(self.placeInQueue), 20)
        print(self.root.children[0].children)
        print(self.root.ids.screenChanger)
        # return sc


if __name__ == '__main__':
    MyLineMakerApp().run()
