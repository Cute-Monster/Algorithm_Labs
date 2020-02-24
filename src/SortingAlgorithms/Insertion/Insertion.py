"""
This is a pure python implementation of the insertion sort algorithm
For doctests run following command:
python -m doctest -v insertion_sort_normal_collection.py
or
python3 -m doctest -v insertion_sort_normal_collection.py
For manual testing run:
python insertion_sort_normal_collection.py
"""


def insertion_sort(collection):
    """Pure implementation of the insertion sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> insertion_sort_normal_collection([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> insertion_sort_normal_collection([])
    []
    >>> insertion_sort_normal_collection([-2, -5, -45])
    [-45, -5, -2]
    """
    loop_counter = 0
    for loop_index in range(1, len(collection)):
        loop_counter = loop_counter + 1
        insertion_index = loop_index
        while (
            insertion_index > 0
            and collection[insertion_index - 1].salary > collection[insertion_index].salary
        ):
            loop_counter = loop_counter + 1
            collection[insertion_index], collection[insertion_index - 1] = (
                collection[insertion_index - 1],
                collection[insertion_index],
            )
            insertion_index -= 1

    return collection, loop_counter


def insertion_sort_normal_collection(collection):
    """Pure implementation of the insertion sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> insertion_sort_normal_collection([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> insertion_sort_normal_collection([])
    []
    >>> insertion_sort_normal_collection([-2, -5, -45])
    [-45, -5, -2]
    """

    for loop_index in range(1, len(collection)):
        insertion_index = loop_index
        while (
            insertion_index > 0
            and collection[insertion_index - 1] > collection[insertion_index]
        ):
            collection[insertion_index], collection[insertion_index - 1] = (
                collection[insertion_index - 1],
                collection[insertion_index],
            )
            insertion_index -= 1

    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(insertion_sort_normal_collection(unsorted))
