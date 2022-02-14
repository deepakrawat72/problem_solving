from simple_linked_list import Node


def detect_loop(node):
    curr_node = node
    nodes_set = set()
    while curr_node.next is not None:
        if curr_node.key in nodes_set:
            return True
        nodes_set.add(curr_node.key)
        curr_node = curr_node.next

    return False


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    #head.next.next.next = head.next

    print(detect_loop(head))
