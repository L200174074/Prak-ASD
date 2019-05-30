from stack import Stack

# No.1
def cetakHexa():
    a = int(input("Masukkan bilangan = " ))
    hexa = Stack()
    hexlist = "0123456789ABCDEF"
    while a!=0:
        sisa = a%16
        a = a//16
        hexa.push(hexlist[sisa])
    hasil=""
    for i in range(len(hexa)):
        hasil = hasil+str(hexa.pop())
    return hasil

print(cetakHexa())

# No.2
nilai = Stack()
for i in range(16):
    if i % 3 == 0:
        nilai.push(i)
print(nilai.items)

# No.3
nilai = Stack()
for i in range(16):
    if i % 3 == 0:
        nilai.push(i)
    elif i % 4 == 0:
        nilai.pop() 
print(nilai.items)

# No. 4
def getFrontMost(self, item):
    self.items.append(item)
    
def getRearMost(self, item):
    self.items.insert(0,item)
    
# No. 5
import heapq

class PriorityQueue(object):
    def __init__(self):
        self.qlist=[]
        self._index = 0

    def __len__(self):
        return len(self.qlist)

    def isEmpty(self):
        return len(self)==0

    def enqueue(self, item, priority):
        heapq.heappush(self.qlist, (priority, self._index, item))
        self._index += 1

    def dequeue(self):
        return heapq.heappop(self.qlist)[-1]

class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

q = PriorityQueue()
q.enqueue('Semangka', 5)
q.enqueue('Jeruk', 2)
q.enqueue('Stroberry', 1)
q.enqueue('Alpukat', 3)
q.enqueue('Pepaya', 4)