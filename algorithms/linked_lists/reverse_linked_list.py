from simple_linked_list import Node
from linked_list_operations import traverse


def reverse_ll(node):
    current = node
    prev_node = None

    while current is not None:
        next_node = current.next
        current.next = prev_node
        prev_node = current

        current = next_node

    node = prev_node

    return node


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    traverse(head)
    print("\nReversed linked list")
    head = reverse_ll(head)
    traverse(head)
