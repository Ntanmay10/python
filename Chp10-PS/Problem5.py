# write a class train which has methods to book ticket, get status(no of seat), and get fare info of train running under indian railways

import os
from random import randint
os.system("cls")


class train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def bookTickets(self, fromLoc, toLoc):
        print(f"Ticket is booked in train no: {
              self.trainNo} travelling from {fromLoc} to {toLoc} ")

    def getStatus(self, fromLoc, toLoc):
        print(f"Train no: {
            self.trainNo} travelling from {fromLoc} to {toLoc} is running successfully")

    def getFare(self, fromLoc, toLoc):
        print(f"Ticket fare of train no: {
            self.trainNo} travelling from {fromLoc} to {toLoc} is {randint(222, 555)}")


t = train(12399)
t.bookTickets("Rampur", "Kolkata")
t.getStatus("Rampur", "Kolkata")
t.getFare("Rampur", "Kolkata")
