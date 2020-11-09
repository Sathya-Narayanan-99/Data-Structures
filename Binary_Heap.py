class BinaryHeap():
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, data):
        self.heap.append(data)
        self.bubbleUp(self.size)
        self.size += 1

    def pop(self):
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.heap.pop()
        self.bubbleDown(0)

    def isempty(self):
        return self.size == 0

    def minchild(self, index):
        if index * 2 + 2 > self.size:
            return index * 2 + 1
        if index * 2 + 1 < index * 2 + 2:
            return index * 2 + 1
        else:
            return index * 2 + 2

    def bubbleUp(self, index):
        while index > 0:
            if self.heap[index] < self.heap[(index - 1) // 2]:
                temp = self.heap[index]
                self.heap[index] = self.heap[(index - 1) // 2]
                self.heap[(index - 1) // 2] = temp
            index = (index - 1) // 2

    def bubbleDown(self, index):
        while index * 2 + 1 <= self.size - 1:
            mc = self.minchild(index)
            if self.heap[index] < self.heap[mc]:
                temp = self.heap[index]
                self.heap[index] = self.heap[mc]
                self.heap[mc] = temp
            index = mc

    def display(self):
        for data in self.heap:
            print(data, end=' ')
        print()


if __name__ == '__main__':
    h = BinaryHeap()
    h.display()
    print(h.isempty())
    h.insert(10)
    h.insert(13)
    h.display()
    h.insert(9)
    h.display()
    h.pop()
    h.display()
    print(h.isempty())
    h.pop()
    h.display()
