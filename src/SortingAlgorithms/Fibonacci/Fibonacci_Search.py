"""
@params
arr: input array
val: the value to be searched
output: the index of element in the array or -1 if not found
return 0 if input array is empty
"""


def FibonacciSearch(lys, val):
    """
        >>> FibonacciSearch([1,6,7,0,0,0], 6)
        1
        >>> FibonacciSearch([1,-1, 5, 2, 9], 10)
        -1
        >>> FibonacciSearch([], 9)
        0
        """
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while fibM < len(lys):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    loop = 0
    while fibM > 1:
        loop = loop + 1
        # print(loop)
        i = min(index + fibM_minus_2, (len(lys) - 1))
        if lys[i].salary < val:
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif lys[i].salary > val:
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            return i, loop
    if fibM_minus_1 and index < (len(lys) - 1) and lys[index + 1].salary == val:
        return index + 1, loop
    return -1, loop


def FibonacciSearchNormalArray(lys, val):
    """
        >>> FibonacciSearch([1,6,7,0,0,0], 6)
        1
        >>> FibonacciSearch([1,-1, 5, 2, 9], 10)
        -1
        >>> FibonacciSearch([], 9)
        0
        """
    loop_counter = 0
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    if len(lys) is 0:
        return 0, loop_counter
    while fibM < len(lys):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    while fibM > 1:
        i = min(index + fibM_minus_2, (len(lys) - 1))
        if lys[i] < val:
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            loop_counter = loop_counter + 1
            index = i
        elif lys[i] > val:
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            loop_counter = loop_counter + 1
        else:
            print(loop_counter + 1)
            return i, loop_counter + 1
    if fibM_minus_1 and index < (len(lys) - 1) and lys[index + 1] == val:
        print(loop_counter + 1)
        return index + 1, loop_counter
    return -1, loop_counter


if __name__ == '__main__':
    listedarray = [1, 152, 14]
    print(FibonacciSearchNormalArray([], 152))
