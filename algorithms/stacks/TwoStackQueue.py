class TwoStackQueue:
    def __init__(self):
        self.__stack1 = []
        self.__stack2 = []

    def enqueue(self, item):
        if len(self.__stack2) == 0:
            self.__stack2.append(item)
        else:
            while len(self.__stack2) > 0:
                last_item = self.__stack2.pop()
                self.__stack1.append(last_item)

            self.__stack2.append(item)

            while len(self.__stack1) > 0:
                last_item = self.__stack1.pop()
                self.__stack2.append(last_item)

    def dequeue(self):
        if len(self.__stack2) != 0:
            return self.__stack2.pop()
        else:
            return -1

    def print(self):
        print(self.__stack2)


if __name__ == '__main__':
    two_stack_queue = TwoStackQueue()
    print("Enqueuing items to queue")
    two_stack_queue.enqueue(10)
    two_stack_queue.enqueue(20)
    two_stack_queue.enqueue(30)
    two_stack_queue.print()
    print(two_stack_queue.dequeue())
    print(two_stack_queue.dequeue())
    two_stack_queue.print()
    two_stack_queue.enqueue(20)
    two_stack_queue.print()
