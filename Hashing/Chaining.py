from LinkedList import LinkedList
class HashChain:
    def __init__(self):
        self.hashtable_size = 10
        self.hashtable = [0] * self.hashtable_size
        for i in range(self.hashtable_size):
            self.hashtable[i]=LinkedList()

    def hashcode(self,key):
        return key % self.hashtable_size

    def insert(self, element):
        i = self.hashcode(element)
        self.hashtable[i].insertsorted(element)

    def search(self, key):
        i = self.hashcode(key)
        return self.hashtable[i].search(key) != -1

    def display(self):
        for i in range(self.hashtable_size):
            print('[', i,']' ,end=' ')
            self.hashtable[i].display()

        print()


H = HashChain()
H.insert(54)
H.insert(23)
H.insert(58)
H.insert(45)
H.insert(44)
H.insert(33)
H.insert(48)
H.insert(65)
H.insert(74)
H.display()


