"""
    TODO:
        1: Script to make data_set file [Done]
        ..... Lab 1 .....
        2: Search algorithms
              :param array
              :param search_value
              :except _is_sorted
              :return index, loop_counter [index is index of element matching search_value]
            1: Secvent search
            2: Binary seacrh [Done]
            3: Fibonacci search [Done]
            4: Interpolation search [Done]
            5: Linked_List search
        3: Print (sum of loop counters)/len(array) for a random element search from array of objects
        ..... Lab 2 .....
        4: Sort algorithms
            1: Bubble sort
            2: Insertion sort
            3: Selection sort
            4: Quick sort
            5: Shell sort
            6: Heap sort
            7: Merge sort
        5: Print loop counters for each sorting algorithm
"""


from src.FileClass.FileClass import File
from src.SomeHelpingDefs import LittleHelpDefs as Helpful
import random

if __name__ == "__main__":
    with open("../../src/ResultTableFiles/Result", "r") as file:
        data = file.readlines()

    unsorted_file_array = Helpful.parse_data_to_array_objects(data, File)
    sorted_file_array = Helpful.sorted_table_file_creator(unsorted_file_array)

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

    """
    Printing step counter for each algorithm with random search position
    """
    print(Helpful.colored("\nStep counter for each algorithm with random search position", "cyan"))
    random_element = random.randint(0, len(sorted_file_array)-1)
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
    print(Helpful.colored("\t\tSum of all algorithms loop counters: ", "magenta") +
          "{}".format(
              Helpful.FibS.FibonacciSearch(sorted_file_array, sorted_file_array[random_element].salary)[1] +
              Helpful.SecvS.Secventional_Search(sorted_file_array, sorted_file_array[random_element].salary)[1] +
              Helpful.BinS.binary_search(sorted_file_array, sorted_file_array[random_element].salary)[1] +
              Helpful.InterpS.interpolation_search(sorted_file_array, sorted_file_array[random_element].salary)[1]
          ))
    """
    Printing algorithms complexity
    """
    algorithms_complexity = Helpful.algorithms_complexity(sorted_file_array)
    print(Helpful.colored("\nComplexity of Algorithms:", "cyan"))
    print(
        Helpful.colored("\tSecventional search algorithm: ", "magenta") + str(algorithms_complexity[0]) +
        Helpful.colored("\n\tInterpolation search algorithm: ", "magenta") + str(algorithms_complexity[1]) +
        Helpful.colored("\n\tBinary search algorithm: ", "magenta") + str(algorithms_complexity[2]) +
        Helpful.colored("\n\tFibonacci search algorithm: ", "magenta") + str(algorithms_complexity[3])
    )

    print(Helpful.colored("\n\t\t..... LAB 2 .....", "green"))
    print(Helpful.colored("Step counter for each sorting algorithm", "cyan"))
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
