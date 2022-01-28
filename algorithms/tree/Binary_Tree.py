import math


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# left -> root -> right (root in middle)
def traverse_inorder(node):
    if node is not None:
        traverse_inorder(node.left)
        print(node.data, end=' ')
        traverse_inorder(node.right)


# root -> left -> right (root at pre)
def traverse_preorder(node):
    if node is not None:
        print(node.data, end=' ')
        traverse_preorder(node.left)
        traverse_preorder(node.right)


# left -> right -> root (root at post)
def traverse_postorder(node):
    if node is not None:
        traverse_postorder(node.left)
        traverse_postorder(node.right)
        print(node.data, end=' ')


# time complexity - ϴ(n)
# space complexity - ϴ(h) -> where h is the height of the tree
def size_of_binary_tree(node):
    if node is None:
        return 0
    else:
        left_size = size_of_binary_tree(node.left)
        right_size = size_of_binary_tree(node.right)
        return left_size + right_size + 1


# time complexity - ϴ(n)
# space complexity - ϴ(h) -> where h is the height of the tree
def maximum_in_binary_tree(node):
    if node is None:
        return -math.inf
    else:
        left_size = maximum_in_binary_tree(node.left)
        right_size = maximum_in_binary_tree(node.right)
        return max(node.data, left_size, right_size)


# time complexity - ϴ(n)
# space complexity - ϴ(h) -> where h is the height of the tree
def find_value(node, key):
    if node is None:
        return False
    if node.data == key:
        return True
    elif find_value(node.left, key):
        return True
    else:
        return find_value(node.right, key)


def find_height(node):
    if node is None:
        return 0
    else:
        left_height = find_height(node.left)
        right_height = find_height(node.right)
        return max(left_height, right_height) + 1


def iterative_inorder_traversal(root):
    if root is None:
        return

    stack = []
    curr = root
    while curr is not None:
        stack.append(curr)
        curr = curr.left

    while len(stack) > 0:
        curr_node = stack.pop()
        print(curr_node.data, end=' ')

        curr_node = curr_node.right

        while curr_node is not None:
            stack.append(curr_node)
            curr_node = curr_node.left


def iterative_preorder_traversal(root):
    if root is None:
        return

    stack = []
    curr = root
    while curr is not None:
        stack.append(curr)
        curr = curr.left

    while len(stack) > 0:
        curr_node = stack.pop()
        print(curr_node.data, end=' ')

        curr_node = curr_node.right

        while curr_node is not None:
            stack.append(curr_node)
            curr_node = curr_node.left


# driver code
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.right = Node(50)
    traverse_inorder(root)
    print()
    traverse_preorder(root)
    print()
    traverse_postorder(root)
    print()
    print(size_of_binary_tree(root))
    print(maximum_in_binary_tree(root))
    print(find_value(root, 20))
    print(find_height(root))
    iterative_inorder_traversal(root)
