'''
Stack source code
'''


class Stack:
    def __init__(self):
        self.stack_list = []

    # Inserts the element onto the stack.
    def push(self, data):
        self.stack_list.append(data)

    # Removes the element from the stack.
    def pull(self):
        self.stack_list.pop()

    # Displays the stack
    def display(self):
        for data in self.stack_list:
            print(data, end=' ')
        print()

    # Returns if the stack is empty.
    def isempty(self):
        return len(self.stack_list) == 0


# Main function
if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.display()
    stack.pull()
    stack.display()
    stack.pull()
    stack.display()
    print(stack.isempty())
    stack.push(10)
    stack.display()
    stack.pull()
    stack.display()
    stack.pull()
    stack.pull()
    stack.pull()
    stack.display()
    print(stack.isempty())
