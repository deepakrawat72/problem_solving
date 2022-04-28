from simple_linked_list import Node
from linked_list_operations import traverse, reverse_ll, append


def sum_ll(node1, node2):
    reversed_ll_1 = reverse_ll(node1)
    reversed_ll_2 = reverse_ll(node2)

    curr_node1 = reversed_ll_1
    curr_node2 = reversed_ll_2
    summed_node = None
    carry_over = 0

    while curr_node1 is not None and curr_node2 is not None:
        value_1 = curr_node1.key
        value_2 = curr_node2.key

        values_sum = value_1 + value_2 + carry_over

        if values_sum > 9:
            summed_value = values_sum % 10
            carry_over = 1
        else:
            summed_value = values_sum

        summed_node = append(summed_node, summed_value)

        curr_node1 = curr_node1.next
        curr_node2 = curr_node2.next

    while curr_node1 is not None:
        value = curr_node1.key + carry_over

        if value > 9:
            carry_over = 1
            summed_node = append(summed_node, value % 10)
        else:
            summed_node = append(summed_node, value)

        curr_node1 = curr_node1.next

    while curr_node2 is not None:
        value = curr_node2.key + carry_over

        if value > 9:
            carry_over = 1
            summed_node.next = Node(value % 10)
        else:
            summed_node.next = Node(value)

        curr_node2 = curr_node2.next

    return reverse_ll(summed_node)


if __name__ == '__main__':
    ll1 = Node(8)
    ll1.next = Node(9)
    ll1.next.next = Node(6)
    ll1.next.next.next = Node(5)

    ll2 = Node(4)
    ll2.next = Node(5)

    print("linked list 1")
    traverse(ll1)
    print("\nlinked list 2")
    traverse(ll2)
    print("\nsummed up linked list")

    ll_summed = sum_ll(ll1, ll2)

    traverse(ll_summed)
