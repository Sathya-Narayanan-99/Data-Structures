'''
Double linked list source code
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    # Adds new node containing 'data' to the end of the linked list.
    def append(self, data):
        cur_node = self.head
        new_node = Node(data)
        if cur_node == None:
            new_node.prev = cur_node
            cur_node = new_node
            self.head = new_node
        else:
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = None
            new_node.prev = cur_node

    # Adds new node containing 'data' to the beginning of the linked list.
    def prepend(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node == None:
            cur_node = new_node
            new_node.prev = None
            self.head = new_node
        else:
            cur_node.prev = new_node
            new_node.next = cur_node
            new_node.prev = None
            self.head = new_node

    # Prints out the linked list.
    def display(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next

    # Returns the length (integer) of the linked list.
    def length(self):
        cur_node = self.head
        node_count = 0
        while cur_node != None:
            cur_node = cur_node.next
            node_count += 1
        return node_count

    # Returns the value of the node at 'index'.
    def get(self, index):
        cur_index = 0
        cur_node = self.head
        if index < 0:
            print("ERROR: Index cannot be NEGATIVE!")
            return
        while cur_node != None:
            if cur_index == index:
                return cur_node.data
            cur_node = cur_node.next
            cur_index += 1

    # Deletes the node at index 'index'.
    def remove(self, index):
        cur_index = 0
        cur_node = self.head
        if self.length() < index:
            print("ERROR: Index out of bounds!")
            return
        while True:
            last_node = cur_node.prev
            next_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                next_node.prev = cur_node.prev
                return
            cur_node = cur_node.next
            cur_index += 1

    # Inserts the node 'node' after the given index 'index'.
    def insert_after(self, index, data):
        if self.length() < index and index < 0:
            print("ERROR: Index out of bounds!")
            return
        cur_index = 0
        cur_node = self.head
        new_node = Node(data)
        while cur_node != None:
            next_node = cur_node.next
            if cur_index == index:
                cur_node.next = new_node
                new_node.prev = cur_node
                new_node.next = next_node
                next_node.prev = new_node
                return
            cur_node = cur_node.next
            cur_index += 1

    # Inserts the node 'node' before the given index 'index'.
    def insert_before(self, index, data):
        if index < 0 and index > self.length() - 1:
            print("ERROR: Index out of bounds!")
            return
        cur_index = 0
        cur_node = self.head
        while cur_node != None:
            if cur_index == index - 1:
                self.insert_after(cur_index, data)
                return
            cur_index += 1
            cur_node = cur_node.next


# Main Function
if __name__ == '__main__':
    linked_list = DoubleLinkedList()
    for i in range(6):
        linked_list.append(i)
    # linked_list.display()
    for i in range(-1, -6, -1):
        linked_list.prepend(i)
    # linked_list.display()
    linked_list.display()
    print('Length is : ', linked_list.length())
    print('Element at the index is : ', linked_list.get(9))
    linked_list.remove(9)
    print("Removed element from index 9")
    linked_list.display()
    linked_list.insert_after(8, 4)
    print("Adding element after index 8")
    linked_list.display()
    linked_list.insert_before(10, 4.5)
    print("Adding element before index 10")
    linked_list.display()
