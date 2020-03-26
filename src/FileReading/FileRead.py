"""
    TODO:
        1: Script to make data_set file [Done]
        ..... Lab 1 .....
        2: Search algorithms
              :param array
              :param search_value
              :except _is_sorted
              :return index, loop_counter [index is index of element matching search_value]
            1: Secvent search [Done]
            2: Binary search [Done]
            3: Fibonacci search [Done]
            4: Interpolation search [Done]
            5: BST search [Done]
        3: Print (sum of loop counters)/len(array) for a random element search from array of objects
        ..... Lab 2 .....
        1: Sort algorithms
            1: Bubble sort [Done]
            2: Insertion sort [Done]
            3: Selection sort [Done]
            4: Quick sort [Done]
            5: Shell sort [Done]
            6: Heap sort [Done]
            7: Merge sort [Done]
        2: Calculating Theoretic complexity of the algorithm [Done]
        3: Calculating Practical complexity of the algorithm [Done]
"""

from src.FileClass.FileClass import File
from src.SomeHelpingDefs import LittleHelpDefs as Helpful
import random
from math import log, log10, log2, pow

import src.ThirdLab.LinkedList.LinkedList as LinkedList
import src.ThirdLab.LinkedList.DoubleLinkedList as DLL
import src.ThirdLab.LinkedList.CircularLinkedList as Circular
import src.ThirdLab.Stack.Stack as Stack
import src.ThirdLab.Queue.Queue as Queue

if __name__ == "__main__":
    with open("../../src/ResultTableFiles/Result", "r") as file:
        data = file.readlines()

    unsorted_file_array = Helpful.parse_data_to_array_objects(data, File)
    sorted_file_array = Helpful.sorted_table_file_creator(unsorted_file_array.copy())
    """
    print(Helpful.colored("\t\t.....LAB 1.....", "green"))
    search_value = int(input("Enter Amount of Salary to Search --> "))

    Helpful.printing_output("Fibonacci", sorted_file_array,
                            Helpful.FibS.FibonacciSearch(sorted_file_array, search_value)[0], search_value)

    Helpful.printing_output("Secventional", sorted_file_array,
                            Helpful.SecvS.Secventional_Search(sorted_file_array, search_value)[0], search_value)

    Helpful.printing_output("Binary", sorted_file_array,
                            Helpful.BinS.binary_search(sorted_file_array, search_value)[0], search_value)

    Helpful.printing_output("Interpolation", sorted_file_array,
                            Helpful.InterpS.interpolation_search(sorted_file_array, search_value)[0], search_value)

    BST_balanced_tree = Helpful.BST.buildBalancedTree(sorted_file_array.copy(), 0, len(sorted_file_array))
    BST_search_result = Helpful.BST.binaryTree.lookup(BST_balanced_tree, search_value)
    Helpful.bst_output_print("BST", BST_search_result, search_value)
    Helpful.BST.loop_counter = 0

    # Printing step counter for each algorithm with random search position

    print(Helpful.colored("\nStep counter for each algorithm with random search position", "cyan"))
    random_element = random.randint(0, len(sorted_file_array) - 1)
    print(sorted_file_array[random_element].name, sorted_file_array[random_element].salary, sep="\t")
    print("\tRandom position is " + Helpful.colored("{}".format(str(random_element)), "red") + ", with value ==> " +
          Helpful.colored("{}".format(str(sorted_file_array[random_element].salary)), "yellow"))
    print(Helpful.colored("\t\tFibonacci algorithm steps: ", "magenta") +
          str(Helpful.FibS.FibonacciSearch(sorted_file_array, sorted_file_array[random_element].salary)[1]))
    print(Helpful.colored("\t\tSecventional algorithm steps: ", "magenta") +
          str(Helpful.SecvS.Secventional_Search(sorted_file_array, sorted_file_array[random_element].salary)[1]))
    print(Helpful.colored("\t\tBinary algorithm steps: ", "magenta") +
          str(Helpful.BinS.binary_search(sorted_file_array, sorted_file_array[random_element].salary)[1]))
    print(Helpful.colored("\t\tInterpolation algorithm steps: ", "magenta") +
          str(Helpful.InterpS.interpolation_search(sorted_file_array, sorted_file_array[random_element].salary)[1]))

    Helpful.BST.binaryTree.lookup(BST_balanced_tree, sorted_file_array[random_element].salary)
    print(Helpful.colored("\t\tBST algorithm steps: ", "magenta") +
          str(Helpful.BST.get_loop_counter()))

    # Printing algorithms complexity

    algorithms_complexity = Helpful.algorithms_complexity(
        obj_array=sorted_file_array,
        bst_balanced_tree=BST_balanced_tree
    )
    print(Helpful.colored("\nPractical Complexity of Algorithms:", "cyan"))
    print(
        Helpful.colored("\tSecventional search algorithm: ", "magenta") + str(algorithms_complexity[0]) +
        Helpful.colored("\n\tInterpolation search algorithm: ", "magenta") + str(algorithms_complexity[1]) +
        Helpful.colored("\n\tBinary search algorithm: ", "magenta") + str(algorithms_complexity[2]) +
        Helpful.colored("\n\tFibonacci search algorithm: ", "magenta") + str(algorithms_complexity[3]) +
        Helpful.colored("\n\tBST search algorithm: ", "magenta") + str(algorithms_complexity[4])
    )

    print(Helpful.colored("\nTheoretic Complexity of Algorithms:", "cyan"))
    print(
        Helpful.colored("\tSecventional search algorithm: ", "magenta") +
        str(len(sorted_file_array) // 2) +
        Helpful.colored("\n\tInterpolation search algorithm: ", "magenta") +
        "{:.2f}".format(log(log(len(sorted_file_array)))) +
        Helpful.colored("\n\tBinary search algorithm: ", "magenta") +
        "{:.2f}".format(log2(len(sorted_file_array))) +
        Helpful.colored("\n\tFibonacci search algorithm: ", "magenta") +
        "{:.2f}".format(log10(len(sorted_file_array))) +
        Helpful.colored("\n\tBST search algorithm: ", "magenta") +
        "{:.2f}".format(log(len(sorted_file_array)))
    )

    print(Helpful.colored("\n\t\t..... LAB 2 .....", "green"))
    print(Helpful.colored("Step counter for each sorting algorithm/ Practical complexity", "cyan"))
    # unsorted_file_array.sort(key=lambda x: x.salary, reverse=True)
    Bubble_sorted = Helpful.BubbleS.bubble_sort(unsorted_file_array.copy())
    print(Helpful.colored("\tBubble_sort loop counter: ", "magenta"),
          Bubble_sorted[1])

    Insertion_sorted = Helpful.InsS.insertion_sort(unsorted_file_array.copy())
    print(Helpful.colored("\tInsertion_sort loop counter: ", "magenta"),
          Insertion_sorted[1])

    Selection_sorted = Helpful.SelS.selection_sort(unsorted_file_array.copy())
    print(Helpful.colored("\tSelection_sort loop counter: ", "magenta"),
          Helpful.SelS.get_loop_counter())

    Quick_sorted = Helpful.QuickS.quick_sort_3partition(
        unsorted_file_array.copy(),
        0,
        len(unsorted_file_array.copy()) - 1,
        0,
        0
    )
    print(Helpful.colored("\tQuick_sort loop counter: ", "magenta"),
          Quick_sorted[1])

    Shell_sorted = Helpful.ShellS.shell_sort(unsorted_file_array.copy())
    print(Helpful.colored("\tShell_sort loop counter: ", "magenta"),
          Helpful.ShellS.get_loop_counter())

    Heap_sorted = Helpful.HeapS.heap_sort(unsorted_file_array.copy())
    print(Helpful.colored("\tHeap_sort loop counter: ", "magenta"),
          Helpful.HeapS.get_loop_counter())

    Merge_sorted = Helpful.MergeS.merge_sort(unsorted_file_array.copy())
    print(Helpful.colored("\tMerge_sort loop counter: ", "magenta"),
          Helpful.MergeS.get_loop_counter())

    print(Helpful.colored("\nTheoretic Complexity of Algorithms:", "cyan"))
    print(
        Helpful.colored("\tBubble sort algorithm: ", "magenta") +
        str(pow(len(sorted_file_array), 2)) +
        Helpful.colored("\n\tHeap sort algorithm: ", "magenta") +
        "{:.2f}".format(len(sorted_file_array) * log(len(sorted_file_array))) +
        Helpful.colored("\n\tInsertion sort algorithm: ", "magenta") +
        "{:.2f}".format(pow(len(sorted_file_array), 2)) +
        Helpful.colored("\n\tMerge sort algorithm: ", "magenta") +
        "{:.2f}".format(len(sorted_file_array) * log(len(sorted_file_array))) +
        Helpful.colored("\n\tQuick sort algorithm: ", "magenta") +
        "{:.2f}".format(len(sorted_file_array) * log(len(sorted_file_array))) +
        Helpful.colored("\n\tSelection sort algorithm: ", "magenta") +
        "{:.2f}".format(pow(len(sorted_file_array), 2)) +
        Helpful.colored("\n\tShell sort algorithm: ", "magenta") +
        "{:.2f}".format(pow(len(sorted_file_array), 2))
    )
    """

    print(Helpful.colored("\t\t.....LAB 3.....", "green"))
    data_to_set = File(
        name="Ghost",
        salary=0,
        position="Test",
        working_years=0,
        kids=0
    )

    circular_linked_list = Circular.CircularLinkedList()
    linked_list = LinkedList.LinkedList()
    double_linked_list = DLL.LinkedList()
    stack = Stack.Stack(
        limit=len(sorted_file_array)
    )
    queue = Queue.Queue()
    double_linked_list.insertHead(sorted_file_array[0])
    for idx, item in enumerate(sorted_file_array):
        circular_linked_list.append(item)
        linked_list.insert_tail(item)
        stack.push(item)
        queue.put(item)
        if idx != 0:
            double_linked_list.insertTail(item)

    # queue.print()
    # print("End Queue")
    # items = queue.get()
    # queue.search(9810)

    # double_linked_list.display()
    # print("End Double-LinkedList")
    # double_linked_list.search(9811)
    # double_linked_list.deleteHead()
    #double_linked_list.display()


    # circular_linked_list.print()
    # print("END_Circular")
    # search_circular_item = circular_linked_list.search_for_element(3054)
    # search_circular_item.print_data()


    # linked-list
    # linked_list.insert_in_position(data_to_set, 3)
    # linked_list.print_list()
    # searched_item = linked_list.search(3383)
    # searched_item.print_data()

    # stack = Stack.Stack(
    #     limit=len(sorted_file_array)
    # )
    # for item in sorted_file_array:
    #     stack.push(item)
    #
    # stack.search(
    #     search_item=int(input(
    #         "Input salary to search -->"))
    # )
    # print("")
    # stack.delete_item(
    #     search_item=int(input(
    #         "Input salary to delete -->"))
    # )
    # stack.print()
