class  QueuesArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def enqueue(self,e):
        self._data.append(e)

    def dequeue(self):
        if self.isempty():
            print('Queue is Empty')
            return
        return self._data.pop(0)

    def first(self):
        if self.isempty():
            print('Queue is Empty')

        return self._data[0]

Q = QueuesArray()
Q.enqueue(5)
Q.enqueue(7)
Q.enqueue(12)
Q.enqueue(3)
print(Q._data)
Q.dequeue()
print(Q._data)
print('Length:',len(Q))

print(Q.first())



