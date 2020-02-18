from src.FileClass.FileClass import File
from src.SortingAlgorithms.Fibonacci import Fibonacci_Search
from src.SortingAlgorithms.Secvent import Secventional_Search
from src.SortingAlgorithms.Binary import Binary
from src.SortingAlgorithms.Interpolation import Interpolation
from src.FileReading.SomeHelpingDefs import LittleHelpDefs as Helpful

if __name__ == "__main__":
    with open("../ResultTableFiles/Result", "r") as file:
        data = file.readlines()
    sorted_file = open("../ResultTableFiles/SortedFiles/SortedBySalary.txt", "w")

    unsorted_file_array = Helpful.parse_data_to_array_objects(data, File)
    sorted_file_array = Helpful.sorted_table_file(sorted_file, unsorted_file_array)

    search_value = int(input("Enter Amount of Salary to Search --> "))

    Fibonacci_found_value = Fibonacci_Search.FibonacciSearch(sorted_file_array, search_value)
    Helpful.printing_output("Fibonacci", sorted_file_array, Fibonacci_found_value, search_value)

    Secventional_found_value = Secventional_Search.Secventional_Search(sorted_file_array, search_value)
    Helpful.printing_output("Secventional", sorted_file_array, Secventional_found_value, search_value)

    Binary_found_value = Binary.binary_search(sorted_file_array, search_value)
    Helpful.printing_output("Binary", sorted_file_array, Binary_found_value, search_value)

    Interpolation_found_value = Interpolation.interpolation_search(sorted_file_array, search_value)
    Helpful.printing_output("Interpolation", sorted_file_array, Interpolation_found_value, search_value)

