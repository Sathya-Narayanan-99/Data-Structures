class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None


class Binary_Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.__insert__(self.root, data)

    def __insert__(self, cur_node, data):
        if data < cur_node.data:
            if cur_node.left_child is None:
                cur_node.left_child = Node(data)
                cur_node.left_child.parent = cur_node
            else:
                self.__insert__(cur_node.left_child, data)
        elif data > cur_node.data:
            if cur_node.right_child is None:
                cur_node.right_child = Node(data)
                cur_node.right_child.parent = cur_node
            else:
                self.__insert__(cur_node.right_child, data)
        else:
            print("Data already EXISTS!")

    def search(self, data):
        if self.root != None:
            return self.__search__(self.root, data)
        else:
            return False

    def __search__(self, cur_node, data):
        if data == cur_node.data:
            return True
        elif data < cur_node.data and cur_node.left_child != None:
            return self.__search__(cur_node.left_child, data)
        elif data > cur_node.data and cur_node.right_child != None:
            return self.__search__(cur_node.right_child, data)
        else:
            return False

    def find(self, data):
        if self.root != None:
            return self.__find__(self.root, data)
        else:
            return None

    def __find__(self, cur_node, data):
        if data == cur_node.data:
            return cur_node
        elif data < cur_node.data and cur_node.left_child != None:
            return self.__find__(cur_node.left_child, data)
        elif data > cur_node.data and cur_node.right_child != None:
            return self.__find__(cur_node.right_child, data)

    def remove(self, data):
        if self.search(data):
            return self.__remove__(self.find(data))
        else:
            print("Data to be deleted not found in the TREE!")
            return None

    def __remove__(self, cur_node):

        # Find minimum value in the left subtree
        def __min_value__(n):
            while n.left_child != None:
                n = n.left_child
            return n

        # Find the number of children
        def num_children(n):
            num_child = 0
            if n.left_child != None:
                num_child += 1
            if n.right_child != None:
                num_child += 1
            return num_child

        # Caching the parent node
        cur_node_parent = cur_node.parent
        # Caching the num of children
        cur_node_child = num_children(cur_node)

        # First Case
        if cur_node_child == 0:
            # Removing the node
            if cur_node_parent.left_child == cur_node:
                cur_node_parent.left_child = None
            if cur_node_parent.right_child == cur_node:
                cur_node_parent.right_child = None

        # Second Case
        if cur_node_child == 1:

            # Finding the child
            if cur_node.left_child != None:
                child = cur_node.left_child
            else:
                child = cur_node.right_child

            # Replace the node to be deleted with its child
            if cur_node_parent.left_child == cur_node:
                cur_node_parent.left_child = child
            if cur_node_parent.right_child == cur_node:
                cur_node_parent.right_child = child

            # Updating the parent
            child.parent = cur_node_parent

        # Third Case
        if cur_node_child == 2:
            succesor = __min_value__(cur_node.right_child)

            cur_node.data = succesor.data
            self.__remove__(succesor)

    def height(self):
        if self.root != None:
            return self.__height__(self.root, 0)
        else:
            return 0

    def __height__(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self.__height__(cur_node.left_child, (cur_height + 1))
        right_height = self.__height__(cur_node.right_child, (cur_height + 1))
        return max(left_height, right_height)

    def display(self):
        if self.root is None:
            print("Tree is EMPTY!")
        else:
            self.__display__(self.root)

    def __display__(self, cur_node):
        if cur_node != None:
            self.__display__(cur_node.left_child)
            print(cur_node.data)
            self.__display__(cur_node.right_child)


def fill_tree(tree, num_of_items=100, max_integer=1000):
    from random import randint
    for i in range(num_of_items):
        tree.insert(randint(0, max_integer))
    return tree


def validator(root, min=-2147483648, max=2147483648):  # Integer range
    if root is None:
        return True
    if (root.data > min and
            root.data < max and \
            validator(root.left_child, min, root.data) and \
            validator(root.right_child, root.data, max)):
        return True
    return False


if __name__ == "__main__":
    tree = Binary_Tree()
    # tree = fill_tree(tree)
    tree.insert(10)
    tree.insert(5)
    tree.insert(8)
    tree.insert(11)
    tree.insert(41)
    tree.insert(29)
    tree.insert(66)
    tree.display()
    print("Tree height : ", tree.height())
    print(tree.search(66))
    print(tree.search(65))
    tree.remove(11)
    tree.display()
    print(validator(tree.root))
