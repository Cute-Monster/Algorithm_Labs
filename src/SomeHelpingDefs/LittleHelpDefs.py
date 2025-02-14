from termcolor import colored
from os import path
from src.SearchAlgorithms.Binary import Binary as BinS
from src.SearchAlgorithms.Fibonacci import Fibonacci_Search as FibS
from src.SearchAlgorithms.Interpolation import Interpolation as InterpS
from src.SearchAlgorithms.Secvent import Secventional_Search as SecvS
from src.SearchAlgorithms.BST import BST as BST
from src.SortingAlgorithms.Insertion import Insertion as InsS
from src.SortingAlgorithms.Buble import Buble as BubbleS
from src.SortingAlgorithms.Quick import Quick as QuickS
from src.SortingAlgorithms.Merge import Merge as MergeS
from src.SortingAlgorithms.Shell import Shell as ShellS
from src.SortingAlgorithms.Selection import Selection as SelS
from src.SortingAlgorithms.Heap import Heap as HeapS


def parse_data_to_array_objects(data, file_class):
    """
    Filling array of objects with data taken from file
    :param data: data that was read from the file
    :param file_class: class that will contain data from the line
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


def sorted_table_file_creator(array):
    """
    Sorting given array of objects by salary and writing this sorted array to file
    :param array:
    :return: array: [sorted by salary]
    """
    with open("{}/SortedBySalary.txt".format(path.abspath('ResultTableFiles/SortedFiles')), "w") as file:
        array.sort(key=lambda x: x.salary, reverse=False)
        for item in array:
            file.writelines("{}\t\t{}\t\t{}\t\t{}\t\t{}\n".format(item.name, str(item.salary), item.position,
                                                                  str(item.working_years), str(item.kids)))

    return array


def printing_output(name, array, index, search_value):

    """
    Writing found value to the console which is colored
    :param name: Algorithms name
    :param array: array, at that was searched value
    :param index: index of the array of found value by some algorithms
    :param search_value: value that was searched by the algorithm
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


def bst_output_print(name, item, search_value):
    """
    Prints output of the BST search
    :param name: Algorithms name
    :param item: found item of BST search algorithm
    :param search_value: value that was searched by the algorithm
    :return:
    """
    print(colored("\n{}".format(name), "cyan") + " search result:")

    if item is None:
        print(colored("\tThere are no records with value ", "red") +
              colored("{} ".format(search_value), "green"))
    else:
        print(colored("\tFound person with value matching to ", "yellow") +
              colored("{}".format(search_value), "magenta") +
              colored(" at ", "yellow") +
              colored("#{}".format(False), "green"))
        print("\t" + item.value.name,
              item.value.salary,
              item.value.position,
              item.value.working_years,
              item.value.kids, sep="\t\t")


def printing_array(array):
    """
    Prints given array of objects
    :param array: array that should be printed
    :return:
    """
    for item in array:
        print("\t" + item.name,
              item.salary,
              item.position,
              item.working_years,
              item.kids, sep="\t\t")


def algorithms_complexity(obj_array, bst_balanced_tree):
    """
    Calculating practical algorithms complexity
    :param obj_array: array of objects
    :param bst_balanced_tree: balanced binary tree
    :return: array: array that contains practical complexity of algorithms
    """

    complexity_array = [0, 0, 0, 0, 0]

    for item in obj_array:
        complexity_array[0] = complexity_array[0] + SecvS.Secventional_Search(obj_array, item.salary)[1]
        complexity_array[1] = complexity_array[1] + InterpS.interpolation_search(obj_array, item.salary)[1]
        complexity_array[2] = complexity_array[2] + BinS.binary_search(obj_array, item.salary)[1]
        complexity_array[3] = complexity_array[3] + FibS.fibonacci_search(obj_array, item.salary)[1]
        BST.BinaryTree.lookup(bst_balanced_tree, item.salary)
        complexity_array[4] = complexity_array[4] + BST.get_loop_counter()

    # for idx, item in enumerate(complexity_array):
    #     print("#{} is {}".format(idx, item))

    for idx, item in enumerate(complexity_array):
        complexity_array[idx] = item/50
    return complexity_array
