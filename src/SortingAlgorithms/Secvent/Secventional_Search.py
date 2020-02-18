def Secventional_Search(array, value):
    loop = 0
    if len(array) is 0:
        return 0, loop
    for idx, element in enumerate(array):
        loop = loop + 1
        if element.salary == value:
            index = idx
            return index, loop
    loop = 0
    return -1, loop


def Secventional_Search_in_normal_array(array, value):
    index = 0
    if len(array) is 0:
        return index
    for idx, element in enumerate(array):
        if element is value:
            index = idx
            return index
    index = -1
    return index


if __name__ == '__main__':
    arraytest = [0, 4, 5, 15]
    print(Secventional_Search_in_normal_array(arraytest, 15))