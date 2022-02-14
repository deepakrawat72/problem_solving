from simple_linked_list import Node


def find_nth_node(head, position):
    if head is None:
        return 0

    length = 1

    curr_node = head

    while curr_node.next is not None:
        length += 1
        curr_node = curr_node.next

    temp = head
    curr_pos = 1
    while temp.next is not None:
        position_from_end = (length - curr_pos) + 1
        if position_from_end == position:
            return temp.key

        temp = temp.next
        curr_pos += 1

    return -1


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    # head.next.next.next = head.next

    print(find_nth_node(head, 2))
