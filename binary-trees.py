# Implement a Binary Tree data structure

class Binary_Node():

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def descendants_preorder(self, node):
        print(node.data)
        if node.left:
            descendants_preorder(node.left)
        if node.right:
            descendants_preorder(node.right)

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

    def count_nodes(node):
        count = 1  # Line 1
        if node.left:  # Line 2
            count += count_nodes(node.left)  # Line 3
        if node.right:  # Line 4
            count += count_nodes(node.right)  # Line 5
        return count  # Line 6
 
# STACK
# A: count_nodes(node7) count=5 Line 5
# Return 5

def preorderTraversal(self, root: TreeNode) -> List[int]:
    # return the preorder traversal of its nodes' values.
        if not root:
            return []
        if root:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

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

    # def print_descendants(self, current=None):
    #     if not current:
    #         current = self.root
    #     if current:
    #         print(current.data)
    #         if current.left:
    #             self.print_descendants(current.left)
    #         if current.right:
    #             self.print_descendants(current.right)



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