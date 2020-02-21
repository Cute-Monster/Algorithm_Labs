from termcolor import colored
import src.SortingAlgorithms.Binary.Binary as BinS
import src.SortingAlgorithms.Fibonacci.Fibonacci_Search as FibS
import src.SortingAlgorithms.Interpolation.Interpolation as InterpS
import src.SortingAlgorithms.Secvent.Secventional_Search as SecvS


def parse_data_to_array_objects(data, file_class):
    """
    Filling array of objects with data taken from file
    :param data:
    :param file_class:
    :return: array: [array consisting objects with data taken from file]
    """
    array = []
    for line in data:
        words = line.split()
        array.append(
            file_class(
                words[0],
                words[1],
                words[2],
                words[3],
                words[4],
            )
        )
    return array


def sorted_table_file(file, array):
    """
    Sorting given array of objects by salary
    and writing this sorted array to file
    :param file:
    :param array:
    :return: array: [sorted by salary]
    """
    array.sort(key=lambda x: x.salary, reverse=False)
    for item in array:
        file.writelines("{}\t\t{}\t\t{}\t\t{}\t\t{}\n".format(item.name, str(item.salary), item.position,
                                                              str(item.working_years), str(item.kids)))
    file.close()
    return array


def printing_output(name, array, index, search_value):
    """
    Writing found value to the console which is colored
    :param name:
    :param array:
    :param index:
    :param search_value:
    :return:
    """
    print(colored("\n{}".format(name), "cyan") + " search result:")
    if index is -1:
        print(colored("\tThere are no records with value ", "red") +
              colored("{} ".format(search_value), "green"))
    else:
        print(colored("\tFound person with value matching to ", "yellow") +
              colored("{}".format(search_value), "magenta") +
              colored(" at ", "yellow") +
              colored("#{}".format(index+1), "green"))
        print("\t" + array[index].name,
              array[index].salary,
              array[index].position,
              array[index].working_years,
              array[index].kids, sep="\t\t")


def algorithms_complexity(obj_array):
    complexity_array = [0, 0, 0, 0, 0]
    for item in obj_array:
        complexity_array[0] = complexity_array[0] + SecvS.Secventional_Search(obj_array, item.salary)[1]
        complexity_array[1] = complexity_array[1] + InterpS.interpolation_search(obj_array, item.salary)[1]
        complexity_array[2] = complexity_array[2] + BinS.binary_search(obj_array, item.salary)[1]
        complexity_array[3] = complexity_array[3] + FibS.FibonacciSearch(obj_array, item.salary)[1]
    """
    for idx, item in enumerate(complexity_array):
        print("#{} is {}".format(idx, item))
    """
    for idx, item in enumerate(complexity_array):
        complexity_array[idx] = item/50
    return complexity_array
