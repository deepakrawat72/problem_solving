def sort_stack(stack):
    stack2 = []

    stack_len = len(stack)

    while stack_len > 0:
        item = stack.pop()
        if len(stack2) == 0:
            stack2.append(item)
        else:
            stack2_len = len(stack2)
            if item > stack2[stack2_len - 1]:
                stack2.append(item)
            else:
                no_of_items_added = 0
                while stack2_len > 0 and item < stack2[stack2_len - 1]:
                    stack2_item = stack2.pop()
                    stack.append(stack2_item)
                    stack2_len -= 1
                    no_of_items_added += 1

                stack2.append(item)

                while no_of_items_added > 0:
                    popped_item = stack.pop()
                    stack2.append(popped_item)
                    no_of_items_added -= 1

        stack_len -= 1

    return stack2


if __name__ == '__main__':
    print(sort_stack([41, 3, 32, 2, 11]))
