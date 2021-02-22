import threading as thread
from queues import queues

from Algorithm.RoadRunnable import RoadRunnable
from Algorithm.TrafficLight import TrafficLight
from RoadRunnable import *
from TrafficLight import *

class Simulation:
    def __init__(self):
        self.thread1 = thread
        self.thread2 = thread
        self.thread3 = thread
        self.thread4 = thread
    def initia(self):
            light = TrafficLight()
            for i in range(4):
                roadi = RoadRunnable(i, light)
                roadi.add()
                self.threadi = thread.Thread(target=roadi)
                self.threadi.start()

            # road2 = RoadRunnable(2, light)
            # road3 = RoadRunnable(3, light)
            # road4 = RoadRunnable(4, light)
            # road1.add(car="")
            # road2.add(car="")
            # road3.add(car="")
            # road4.add(car="")





if __name__ == '__main__':
    s = Simulation()
    s.initia()














