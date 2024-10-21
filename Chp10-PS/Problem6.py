# can you change the self paramater inside a class to something else (say "Tanmay")
# Try changing self to slf or Tanmay and see the effects
import os
from random import randint
os.system("cls")


class train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

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