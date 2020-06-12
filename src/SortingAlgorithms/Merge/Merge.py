"""
This is a pure python implementation of the merge sort algorithm
For doctests run following command:
python -m doctest -v merge_sort.py
or
python3 -m doctest -v merge_sort.py
For manual testing run:
python merge_sort.py
"""
loop_counter = 0


def merge_sort(collection):
    global loop_counter
    loop_counter = 0
    loop_counter = loop_counter + 1

    def merge(left, right):
        """merge left and right
        :param left: left collection
        :param right: right collection
        :return: merge result
        """
        global loop_counter
        result = []
        while left and right:
            loop_counter = loop_counter + 1
            result.append(
                (left if left[0].salary <= right[0].salary else right).pop(0)
            )
            # try:
            #     if left[0].salary <= right[0].salary:
            #         result.append(left.pop(0))
            #     else:
            #         result.append(right.pop(0))
            #     # print(result)
            # except AttributeError or IndexError as e:
            #     print(e)
        return result + left + right

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))


def get_loop_counter():
    global loop_counter
    counter = loop_counter
    loop_counter = 0
    return counter


def merge_sort_normal_collection(collection):
    """Pure implementation of the merge sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_sort([])
    []
    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    def merge_normal_collection(left, right):
        """merge left and right
        :param left: left collection
        :param right: right collection
        :return: merge result
        """
        result = []
        while left and right:
            result.append((left if left[0] <= right[0] else right).pop(0))
        return result + left + right

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge_normal_collection(
        merge_sort_normal_collection(collection[:mid]),
        merge_sort_normal_collection(collection[mid:])
    )


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(*merge_sort(unsorted), sep=",")