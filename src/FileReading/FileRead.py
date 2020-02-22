"""
    TODO:
        1: Script to make data_set file [Done]
        2: Search algorithms
            [ :param array
              :param search_value
              :except _is_sorted
              :return index, loop_counter [index is index of element matching search_value]
            ]
            1: Secvent search
            2: Binary seacrh [Done]
            3: Fibonacci search [Done]
            4: Interpolation search [Done]
            5: Linked_List search
        3: Print Sum of loop counters for a random element search from array of objects
"""


from src.FileClass.FileClass import File
from src.SomeHelpingDefs import LittleHelpDefs as Helpful
import random

if __name__ == "__main__":
    with open("../../src/ResultTableFiles/Result", "r") as file:
        data = file.readlines()

    unsorted_file_array = Helpful.parse_data_to_array_objects(data, File)
    sorted_file_array = Helpful.sorted_table_file_creator(unsorted_file_array)

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
