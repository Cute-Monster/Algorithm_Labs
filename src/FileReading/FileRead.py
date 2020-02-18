# import socketserver
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

    file_array = Helpful.parse_data_to_array_objects(data, File)
    file_array = Helpful.sorted_table_file(sorted_file, file_array)

    search_value = int(input("Enter Amount of Salary to Search --> "))

    Fibonacci_found_value = Fibonacci_Search.FibonacciSearch(file_array, search_value)
    Helpful.printing_output("Fibonacci", file_array, Fibonacci_found_value, search_value)

    Secventional_found_value = Secventional_Search.Secventional_Search(file_array, search_value)
    Helpful.printing_output("Secventional", file_array, Secventional_found_value, search_value)

    Binary_found_value = Binary.binary_search(file_array, search_value)
    Helpful.printing_output("Binary", file_array, Binary_found_value, search_value)

    Interpolation_found_value = Interpolation.interpolation_search(file_array, search_value)
    Helpful.printing_output("interpolation", file_array, Interpolation_found_value, search_value)

