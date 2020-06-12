def bubble_sort(collection):
    """Pure implementation of bubble sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> bubble_sort([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]
    >>> bubble_sort([])
    []
    >>> bubble_sort([-2, -45, -5])
    [-45, -5, -2]
    >>> bubble_sort([-23, 0, 6, -4, 34])
    [-23, -4, 0, 6, 34]
    >>> bubble_sort([-23, 0, 6, -4, 34]) == sorted([-23, 0, 6, -4, 34])
    True
    """
    length = len(collection)
    loop_counter = 0
    for i in range(length - 1):
        loop_counter = loop_counter + 1
        swapped = False
        for j in range(length - 1 - i):
            loop_counter = loop_counter + 1
            if collection[j].salary > collection[j + 1].salary:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection, loop_counter


def bubble_sort_normal_collection(collection):
    """Pure implementation of bubble sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> bubble_sort([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]
    >>> bubble_sort([])
    []
    >>> bubble_sort([-2, -45, -5])
    [-45, -5, -2]
    >>> bubble_sort([-23, 0, 6, -4, 34])
    [-23, -4, 0, 6, 34]
    >>> bubble_sort([-23, 0, 6, -4, 34]) == sorted([-23, 0, 6, -4, 34])
    True
    """
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection


if __name__ == "__main__":
    import time

    # user_input = input("Enter numbers separated by a comma:").strip()
    # unsorted = [int(item) for item in user_input.split(",")]
    unsorted = [1, 3, 2, 5, 4, 7, 6, 8]
    start = time.process_time()
    bubble_sorted = bubble_sort_normal_collection(unsorted)
    print(bubble_sorted[0], "  ", bubble_sorted[1], sep=",")
    print(f"Processing time: {time.process_time() - start}")