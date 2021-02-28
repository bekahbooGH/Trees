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
    def print_descendants(self, call_count=0):
        # DFS (Pre-order) //10 5 8 15
        # if self.data != None:
        #     print(self.data)
        #     if self.left:
        #         self.left.print_descendants()
        #     if self.right:
        #         self.right.print_descendants()
        #     return

        # # In-order // 5 8 10 15
        # if self.data != None:
        #     # check left because it's smaller
        #     if self.left:
        #         # before printing check if curr has a left
        #         self.left.print_descendants()
        #     # when it doesn't have a left then print curr value
        #     print(self.data)
        #     # check if there is a self right
        #     if self.right:
        #         # if yes -- call function on self right
        #         self.right.print_descendants()

        # BFS // 10 5 15 8
        if self.data != None:
            if call_count == 0:
                print(self.data)
            if self.left:
                print(self.left.data)
            if self.right:
                print(self.right.data)
            if self.left:
                call_count += 1
                self.left.print_descendants(call_count)
            if self.right:
                call_count += 1
                self.right.print_descendants(call_count)


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