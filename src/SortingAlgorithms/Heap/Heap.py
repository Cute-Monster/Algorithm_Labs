loop_counter = 0


def heapify(unsorted, index, heap_size):
    global loop_counter
    loop_counter = loop_counter + 1
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index].salary > unsorted[largest].salary:
        largest = left_index

    if right_index < heap_size and unsorted[right_index].salary > unsorted[largest].salary:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    """
    Pure implementation of the heap sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> heap_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> heap_sort([])
    []
    >>> heap_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    global loop_counter

    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        loop_counter = loop_counter + 1
        heapify(unsorted, i, n)
    for i in range(n - 1, 0, -1):
        loop_counter = loop_counter + 1
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted


def get_loop_counter():
    global loop_counter
    counter, loop_counter = loop_counter, 0
    return counter


# if __name__ == "__main__":
#     user_input = input("Enter numbers separated by a comma:\n").strip()
#     unsorted = [int(item) for item in user_input.split(",")]
#     print(heap_sort(unsorted))
