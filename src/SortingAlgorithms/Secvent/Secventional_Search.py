def Secventional_Search(array, value):
    index = 0
    if len(array) is 0:
        return index
    for element in array:
        if element.salary is value:
            index = element.denominator
            return index
    index = -1
    return index


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