# This is a small project to create an app alternative to physically waiting in line after covid 19
Built during the TechTalentSouth Data Science class of Summer 2020 with the help of Gary Jackson
# todo:
# SERVERSIDE:
1. firebase streaming/realtime rest api to send json data of who is waiting in which line (NOT POLLING)
2. simple first in, first out database interface
3. there must be some functionality to accept someone from the line on the owner side, or to remove them if they don't show up
# CLIENTSIDE:
1. simple ui with landing screen just as a button to open camera to scan logo and start waiting in line
2. swipe left for business owner mode to take picture of logo and start a new virtual line
3. waiting in line screen with view of everyone currently waiting in line and an indication of where you are

# Ideas and other concepts:
* how can we uniquely identify each instance of the app without the end user having to login and make an account
* does the business owner mode need to be able to pick which parties it currently has availability / capacity for
* does the end user need a way to indicate size of party
* estimated wait time

# ESSENTIAL FEATURES:
1. [ ] MANAGE LINE SCREEN WITH OPTION TO ACCEPT A CUSTOMER OR REMOVE THEM
2. [X] OPTION TO DELETE LINE 
3. [ ] WAIT LINE SCREEN WITH VISUAL REPRESENTATION OF PEOPLE AHEAD OF YOU IN LINE
4. [ ] NUMBER IN LINE AND A DIFFERENT COLORED ICON FOR WHERE YOU ARE
5. [ ] NOTIFICATION TO CUSTOMER WHEN IT IS THEIR TURN IN LINE NEW SCREEN FOR BEING ACCEPTED
6. [X] PUT DECLARATIONS IN IMPORTED FILE 
7. [X] PUT AUTH KEYS IN IMPORTED FILE 
8. [ ] GENERAL CODE CLEAN UP (I am new to Kivy and much of the markup might not be necessary)
9. [X] POLLING ON TIMER TO REFRESH PLACE IN QUEUE EVERY 20 SECONDS OR SO
10. [ ] TRY BLOCK TO SEE IF WE CAN JOIN A CERTAIN QUEUE

NICE FEATURES TO ADD:
1. [ ] DROP DOWN FOR CURRENTLY CREATED QUEUES (UNNECESSARY IF IMAGE SCANNER IS IMPLEMENTED BUT NICE OTHERWISE)
2. [ ] IMAGE SCANNER (SENDEX OR TENSORFLOW OR OPENCV OR IBM VISUAL INSIGHTS)
3. [ ] ANIMATIONS OF WALKING TO SCREENS OR WAITING
4. [ ] AVERAGE WAIT TIME

General Database schema:

    # Database functions (CRUM)

    # Schema:
    #   {
    #       "queueName": [
    #           "deviceId",
    #           "deviceId2"
    #       ]
    #
    #   }
    #
    #
    # [
    #   {
    #       "deviceId": "",
    #       "queue": "",
    #       "joinTime": ""
    #   }
    # ]
