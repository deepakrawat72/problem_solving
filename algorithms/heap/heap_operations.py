def build_max_heap(arr):
    heap = []
    for item in arr:
        max_heapify(heap, item)

    return heap


def build_min_heap(arr):
    heap = []
    for item in arr:
        min_heapify(heap, item)

    return heap


def max_heapify(heap, item):
    heap.append(item)
    i = len(heap) - 1
    if i == 0:
        return

    while i > 0:
        parent = i // 2

        if heap[parent] < heap[i]:
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent
        else:
            return


def min_heapify(heap, item):
    heap.append(item)
    i = len(heap) - 1
    if i == 0:
        return

    while i > 0:
        parent = i // 2

        if heap[parent] > heap[i]:
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent
        else:
            return


if __name__ == '__main__':
    print(build_max_heap([3, 1, 7, 9, 10, 12, 4]))
    print(build_max_heap([20, 10, 30, 5, 50, 40]))
    print(build_min_heap([3, 1, 7, 9, 10, 12, 4]))
