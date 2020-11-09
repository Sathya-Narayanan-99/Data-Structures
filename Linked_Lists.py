'''
Single linked list source code
'''


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = Node()

    # Adds new node containing 'data' to the end of the linked list.
    def append(self, data):
        cur = self.head
        new_node = Node(data)
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    # Prints out the linked list in traditional Python list format.
    def display(self):
        node_list = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            node_list.append(cur.data)
        print(node_list)

    # Returns the length (integer) of the linked list.
    def length(self):
        cur = self.head
        node_count = 0
        while cur.next != None:
            cur = cur.next
            node_count += 1
        return node_count

    # Returns the value of the node at 'index'.
    def get(self, index):
        index += 1
        if self.length() < index:
            print("ERROR: Index out of bounds!")
            return
        cur_index = 0
        cur = self.head
        while True:
            if cur_index == index:
                return cur.data
            cur = cur.next
            cur_index += 1

    # Deletes the node at index 'index'.
    def remove(self, index):

        if self.length() < index:
            print("ERROR: Index out of bounds!")
            return
        cur_index = 0
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if cur_index == index:
                last_node.next = cur.next
                return
            cur_index += 1

    # Inserts the node 'node' at index 'index'.
    def insert(self, index, data):
        if index < 0:
            print("ERROR: Index cannot be NEGATIVE!")
            return
        if self.length() < index:
            print("ERROR: Index out of bounds!")
            return
        new_node = Node(data)
        cur_index = 0
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if cur_index == index:
                last_node.next = new_node
                new_node.next = cur
                return
            cur_index += 1

    # Sets the data at index 'index' equal to 'data'.
    def set_data(self, index, data):
        if index < 0:
            print("ERROR: Index cannot be NEGATIVE!")
            return
        if self.length() < index:
            print("ERROR: Index out of bounds!")
            return
        cur_index = 0
        cur = self.head
        while True:
            cur = cur.next
            if cur_index == index:
                cur.data = data
                return
            cur_index += 1


if __name__ == '__main__':
    linked_list = Linked_list()
    for i in range(6):
        linked_list.append(i)
        linked_list.display()
    print('Length is : ', linked_list.length())
    print('Element at the index is : ', linked_list.get(2))
    linked_list.remove(2)
    linked_list.display()
    linked_list.insert(2, -2)
    linked_list.display()
    linked_list.set_data(2, 2)
    linked_list.display()
