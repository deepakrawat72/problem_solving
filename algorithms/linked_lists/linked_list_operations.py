from simple_linked_list import Node


def traverse(h):
    curr = h
    while curr is not None:
        print(curr.key, end=" ")
        curr = curr.next


def search(h, element):
    curr = h
    position = 1
    while curr is not None:
        if element == curr.key:
            return position

        position += 1
        curr = curr.next

    return -1


def prepend(h, element):
    node_to_prepend = Node(element)
    node_to_prepend.next = h
    return node_to_prepend


def append(h, element):
    node_to_append = Node(element)
    curr = head
    while curr.next is not None:
        curr = curr.next

    curr.next = node_to_append

    return h


def insert_at(h, element, pos):
    node_to_append = Node(element)
    p = 2
    curr = head
    while curr is not None:
        if p == pos:
            break
        p += 1
        curr = curr.next

    if curr.next is None:
        curr.next = node_to_append
    else:
        temp = curr.next
        curr.next = node_to_append
        node_to_append.next = temp

    return h


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
    head = Node(30)
    head.next = Node(40)
    head.next.next = Node(50)
    print("Before prepending items to linked list")
    traverse(head)
    print("\nSearching item in linked list")
    print("Item not found" if search(head, 40) == -1 else "Item found at " + str(search(head, 40)) + " position")
    head = prepend(head, 20)
    head = prepend(head, 10)
    print("After prepending items to linked list")
    traverse(head)
    head = append(head, 60)
    head = append(head, 70)
    print("\nAfter appending items to linked list")
    traverse(head)
    head = insert_at(head, 35, 3)
    print("\nAfter inserting item - 35 at position 3")
    traverse(head)
    head = insert_at(head, 80, 9)
    print("\nAfter inserting item - 35 at position 3")
    traverse(head)
    print("\nReversing Linked List")
    head = reverse_ll(head)
    traverse(head)
