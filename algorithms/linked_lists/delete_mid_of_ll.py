from simple_linked_list import Node


def delete_mid(node):
    s_ptr = node
    f_ptr = node
    prev_node = None

    while f_ptr and f_ptr.next:
        prev_node = s_ptr
        s_ptr = s_ptr.next
        f_ptr = f_ptr.next.next

    prev_node.next = s_ptr.next

    return node


def traverse(h):
    curr = h
    while curr is not None:
        print(curr.key)
        curr = curr.next


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    head = delete_mid(head)
    traverse(head)

    print("=====")
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)

    head1 = delete_mid(head1)

    traverse(head1)
