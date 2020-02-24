
def quick_sort(collection):
    """Pure implementation of quick sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    length = len(collection)
    if length <= 1:

        return collection
    else:
        # Use the last element as the first pivot
        pivot = collection.pop()
        # Put elements greater than pivot in greater list
        # Put elements lesser than pivot in lesser list
        greater, lesser = [], []
        for element in collection:
            if element > pivot:
                greater.append(element)
            else:
                lesser.append(element)
        print(quick_sort(lesser) + [pivot] + quick_sort(greater))
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


def quick_sort_3partition(sorting, left, right, check, loop_count):
    global loop_counter
    loop_counter = 0
    loop_counter = loop_counter + loop_count
    # print(check)
    if right <= left:
        loop_counter = loop_counter + 1
        return
    a = i = left
    b = right
    pivot = sorting[left].salary
    while i <= b:
        loop_counter = loop_counter + 1
        if sorting[i].salary < pivot:
            sorting[a], sorting[i] = sorting[i], sorting[a]
            a += 1
            i += 1
        elif sorting[i].salary > pivot:
            sorting[b], sorting[i] = sorting[i], sorting[b]
            b -= 1
        else:
            i += 1
    # print("before 1:", loop_counter)
    quick_sort_3partition(sorting, left, a - 1, 1, loop_counter)
    # print("before 2:", loop_counter)
    quick_sort_3partition(sorting, b + 1, right, 2, loop_counter)
    return sorting, loop_counter


def quick_sort_3partition_normal_collection(sorting, left, right, check, loop_count):
    global loop_counter
    loop_counter = 0
    loop_counter = loop_counter + loop_count
    print(check)
    if right <= left:
        loop_counter = loop_counter + 1
        return
    a = i = left
    b = right
    pivot = sorting[left]
    while i <= b:
        loop_counter = loop_counter + 1
        if sorting[i] < pivot:
            sorting[a], sorting[i] = sorting[i], sorting[a]
            a += 1
            i += 1
        elif sorting[i] > pivot:
            sorting[b], sorting[i] = sorting[i], sorting[b]
            b -= 1
        else:
            i += 1
    print("before 1:", loop_counter)
    quick_sort_3partition_normal_collection(sorting, left, a - 1, 1, loop_counter)
    print("before 2:", loop_counter)
    quick_sort_3partition_normal_collection(sorting, b + 1, right, 2, loop_counter)
    return sorting, loop_counter


if __name__ == "__main__":

    unsorted = [5, 1, 8, 7, 6, 2, 9, 0]
    unsorted1 = [5, 1, 8, 7, 6, 2, 9, 0]
    # quick_sort_3partition(unsorted, 0, len(unsorted) - 1, 0)
    # quick_sort(unsorted1)
    # print(quick_sort_3partition(unsorted, 0, len(unsorted) - 1, 0))
    sorted = quick_sort_3partition(unsorted, 0, len(unsorted) - 1, 0, 0)
    print("sorted: ", sorted, "Loop_counter: ", loop_counter)
