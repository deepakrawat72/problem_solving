class Node:
    def __init__(self, k):
        self.key = k
        self.next = None

if __name__ == '__main__':
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
