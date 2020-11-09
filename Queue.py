'''
Queue source code
'''


class Queue:
    def __init__(self):
        self.qlist = []

    # Inserts the element onto the queue.
    def push(self, data):
        self.qlist.append(data)

    # Removes the element from the queue.
    def pop(self):
        self.qlist.pop(0)

    # Displays the queue.
    def display(self):
        for data in self.qlist:
            print(data, end=' ')
        print()

    # Returns if the queue is empty.
    def isempty(self):
        return len(qlist) == 0


# Main function
if __name__ == '__main__':
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)
    queue.display()
    queue.pop()
    queue.display()
    queue.pop()
    queue.display()
    queue.pop()
    queue.display()
    queue.push(6)
    queue.display()
    queue.pop()
    queue.display()
