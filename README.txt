# This is a small project to create an app alternative to physically waiting in line after covid 19
# Built during the TechTalentSouth Data Science class of Summer 2020 with the help of Gary Jackson
# todo:
# SERVERSIDE:
# 1. firebase streaming/realtime rest api to send json data of who is waiting in which line (NOT POLLING)
# 2. simple first in, first out database interface
# 3. there must be some functionality to accept someone from the line on the owner side, or to remove them if
#       they don't show up
# CLIENTSIDE:
# 4. simple ui with landing screen just as a button to open camera to scan logo and start waiting in line
# 5. swipe left for business owner mode to take picture of logo and start a new virtual line
# 6. waiting in line screen with view of everyone currently waiting in line and an indication of where you are
#
# ideas and other concepts:
# how can we uniquely identify each instance of the app without the end user having to login and make an account
# does the business owner mode need to be able to pick which parties it currently has availability / capacity for
# does the end user need a way to indicate size of party
# estimated wait time

ESSENTIAL FEATURES:
MANAGE LINE SCREEN WITH OPTION TO ACCEPT A CUSTOMER OR REMOVE THEM
OPTION TO DELETE LINE X
WAIT LINE SCREEN WITH VISUAL REPRESENTATION OF PEOPLE AHEAD OF YOU IN LINE
NUMBER IN LINE AND A DIFFERENT COLORED ICON FOR WHERE YOU ARE
NOTIFICATION TO CUSTOMER WHEN IT IS THEIR TURN IN LINE NEW SCREEN FOR BEING ACCEPTED
PUT DECLARATIONS IN IMPORTED FILE X
PUT AUTH KEYS IN IMPORTED FILE X
GENERAL CODE CLEAN UP
POLLING ON TIMER TO REFRESH PLACE IN QUEUE EVERY 20 SECONDS OR SO
TRY BLOCK TO SEE IF WE CAN JOIN A CERTAIN QUEUE

NICE FEATURES TO ADD:
DROP DOWN FOR CURRENTLY CREATED QUEUES (UNNECESSARY IF IMAGE SCANNER IS IMPLEMENTED BUT NICE OTHERWISE)
IMAGE SCANNER (SENDEX OR TENSORFLOW OR OPENCV OR IBM VISUAL INSIGHTS)
ANIMATIONS OF WALKING TO SCREENS OR WAITING
AVERAGE WAIT TIME

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
