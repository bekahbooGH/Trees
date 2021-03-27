# Implement a Binary Tree data structure

class Binary_Node():

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def descendants_preorder(self):
        print(self.data)
        if self.left:
            self.left.descendants_preorder()
        if self.right:
            self.right.descendants_preorder()

    def descendants_inorder(self, node):
        if node.left:
            descendants_inorder(node.left)
        print(node.data)
        if node.right:
            descendants_inorder(node.right)
    
    def descendants_postorder(self, node):
        if node.left:
            descendants_postorder(node.left)
        if node.right:
            descendants_postorder(node.right)
        print(node.data)

    
# OUTPUT: 7 1 34 2 0

# STACK

    def count_nodes(self):
        count = 1  # Line 1
        if self.left:  # Line 2
            count += count_nodes(self.left)  # Line 3
        if self.right:  # Line 4
            count += count_nodes(self.right)  # Line 5
        return count  # Line 6

    def preorderTraversal(self, root):
    #  -> List[int]:
        # return the preorder traversal of its nodes' values.
            if not root:
                return []
            if root:
                return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def preorderTraversal(self, root):
    # -> List[int]:
        if not root:
            return []
        # if root:
        #     return root.val + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        print("String: root.right")
        print(root.right)
        print("Self.preorderTraversal")
        print(self.preorderTraversal(root.right))
        print("type preorder Traversal")
        print(type(self.preorderTraversal(root.right)))

    def inorderTraversal(self, root):
    # -> List[int]:
            # if root == None:
            root_list = []
            def fxn(root):
                if root == None:
                    return root_list
                else:
                    fxn(root.left)
                    root_list.append(root.val)
                    fxn(root.right)
            fxn(root)
            return root_list


class Binary_Tree():

    def __init__(self, root=None):
        self.root = root

    def add_node(self, node):
        # first check to see if the root of our tree is empty
        if self.root == None:
            self.root = node
            return
        else:
            def check_children(parent=self.root):
                if not parent.left:
                    parent.left = node
                    return
                if not parent.right:
                    parent.right = node
                    return
                check_children(parent.left)
            check_children()

    # Replace a node
    def replace_node(self, node_to_replace, new_node):

        nodes_to_visit = [self.root]
        # current = self.root
        # [9]
        while nodes_to_visit:
            current = nodes_to_visit.pop(0)  # 9
            if current.data == node_to_replace.data:  # 9 == 8
                node_to_replace.data = new_node.data
                return
            else:
                nodes_to_visit.extend([current.left, current.right])
                print(nodes_to_visit)

node10 = Binary_Node(10)
b_tree = Binary_Tree()
b_tree.add_node(node10)
# print(root)
node5 = Binary_Node(5)
b_tree.add_node(node5)
node8 = Binary_Node(8)
b_tree.add_node(node8)
node15 = Binary_Node(15)
b_tree.add_node(node15)
# b_tree.print_descendants()
# b_tree.descendants_preorder(node10)
# b_tree.descendants_inorder(node10)
# b_tree.descendants_postorder(node10)
node10.descendants_preorder()

# STACK
# A: count_nodes(node7) count=5 Line 5
# Return 5
node7 = Binary_Node(7)
b_tree.add_node(node7)
node7.count_nodes()
