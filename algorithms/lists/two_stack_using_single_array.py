class TwoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, item):
        self.top1 += 1
        if self.top1 < self.top2:
            self.arr[self.top1] = item
        else:
            print("Stack Overflow ")
            exit(1)

    def push2(self, item):
        self.top2 -= 1
        if self.top2 > self.top1:
            self.arr[self.top2] = item
        else:
            print("Stack Overflow ")
            exit(1)

    def pop1(self):
        if self.top1 != -1:
            popped_item = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 -= 1
            return popped_item
        else:
            print("Stack Underflow ")
            exit(1)

    def pop2(self):
        if self.top2 != self.size:
            popped_item = self.arr[self.top2]
            self.arr[self.top2] = None
            self.top2 += 1
            return popped_item
        else:
            print("Stack Underflow ")
            exit(1)


if __name__ == '__main__':
    two_stacks = TwoStacks(n=5)
    two_stacks.push1(1)
    two_stacks.push2(5)

    print(two_stacks.arr)

    two_stacks.push1(2)
    two_stacks.push1(3)
    two_stacks.push1(4)

    print(two_stacks.arr)

    two_stacks.pop2()
    print(two_stacks.arr)

    two_stacks.push2(4)

    print(two_stacks.arr)

    print(two_stacks.top1)
    print(two_stacks.pop1())
    print(two_stacks.pop1())
    print(two_stacks.pop1())
    print(two_stacks.pop1())
    print(two_stacks.pop1())

