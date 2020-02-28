from termcolor import colored
import src.SearchAlgorithms.Binary.Binary as BinS
import src.SearchAlgorithms.Fibonacci.Fibonacci_Search as FibS
import src.SearchAlgorithms.Interpolation.Interpolation as InterpS
import src.SearchAlgorithms.Secvent.Secventional_Search as SecvS
import src.SearchAlgorithms.BST.BST as BST
import src.SortingAlgorithms.Insertion.Insertion as InsS
import src.SortingAlgorithms.Buble.Buble as BubbleS
import src.SortingAlgorithms.Quick.Quick as QuickS
import src.SortingAlgorithms.Merge.Merge as MergeS
import src.SortingAlgorithms.Shell.Shell as ShellS
import src.SortingAlgorithms.Selection.Selection as SelS
import src.SortingAlgorithms.Heap.Heap as HeapS



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



def sorted_table_file_creator(array):
    """
    Sorting given array of objects by salary
    and writing this sorted array to file
    :param array:
    :return: array: [sorted by salary]
    """
    file = open("../ResultTableFiles/SortedFiles/SortedBySalary.txt", "w")
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


def bst_output_print(name, item, search_value):
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
    for item in array:
        print("\t" + item.name,
              item.salary,
              item.position,
              item.working_years,
              item.kids, sep="\t\t")


def algorithms_complexity(obj_array, bst_balanced_tree):
    complexity_array = [0, 0, 0, 0, 0]
    for item in obj_array:
        complexity_array[0] = complexity_array[0] + SecvS.Secventional_Search(obj_array, item.salary)[1]
        complexity_array[1] = complexity_array[1] + InterpS.interpolation_search(obj_array, item.salary)[1]
        complexity_array[2] = complexity_array[2] + BinS.binary_search(obj_array, item.salary)[1]
        complexity_array[3] = complexity_array[3] + FibS.FibonacciSearch(obj_array, item.salary)[1]
        BST.binaryTree.lookup(bst_balanced_tree, item.salary)
        complexity_array[4] = complexity_array[4] + BST.get_loop_counter()

    for idx, item in enumerate(complexity_array):
        print("#{} is {}".format(idx, item))

    for idx, item in enumerate(complexity_array):
        complexity_array[idx] = item/50
    return complexity_array
