import threading as threading
class TrafficLight:
    def __init__(self):
        pass

    def turngreenon(self,rnumber):
        print(f"Light is green by road  {rnumber} \n"
              f"Wating for road {rnumber} car to clear intersection")
        for i in range(10,0,-1):
            print(i,end=" ")
            try:
                threading.Timer(10,i)
            except InterruptedError:
                return
        print()





