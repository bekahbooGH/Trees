# Implement a Binary Search Tree Data Structure

class Bst_Node():

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # Methods to add
    # Insert node
    def insert_node(self, value):
        if value < self.data:
            if self.left == None:
                self.left = Bst_Node(value)
                return
            else:
                self.left.insert_node(value)
        else:
            if self.right == None:
                self.right = Bst_Node(value)
                return
            else:
                self.right.insert_node(value)

    # Print all nodes
    def print_descendants(self):
        # DFS
        if self.data != None:
            print(self.data)
            if self.left:
                self.left.print_descendants()
            if self.right:
                self.right.print_descendants()
            return


class Bs_Tree():

    def __init__(self, root=None):
        self.root = root


# root = Node(15)
# root.insert(5) // 5 < 15 ??? YES
node10 = Bst_Node(10)
root = Bs_Tree(node10).root
root.insert_node(5)
root.insert_node(8)
root.insert_node(15)
root.print_descendants()