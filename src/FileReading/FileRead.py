# import socketserver
from src.FileClass.FileClass import File
from src.SortingAlgorithms import Fibonacci


def get_data_from_file():
    with open("../ResultTableFiles/Result", "r+", ) as f:
        data = f.readlines()
    array = []
    for line in data:
        words = line.split()
        array.append(
            File(
                words[0],
                words[1],
                words[2],
                words[3],
                words[4],
            )
        )
    f.close()
    return array


def sorted_table_file(array):
    sorted_file = open("../ResultTableFiles/SortedFiles/SortedBy{}.txt".format("Salary"), "w")
    array.sort(key=lambda x: x.salary, reverse=False)
    for item in file_array:
        sorted_file.writelines("{}\t\t{}\t\t{}\t\t{}\t\t{}\n".format(item.name, str(item.salary), item.position,
                                                                     str(item.working_years), str(item.kids)))
    return array


if __name__ == "__main__":

    file_array = get_data_from_file()
    file_array = sorted_table_file(file_array)

    search_value = int(input("Enter Search Value [ Salary or working years or kids counter ] --> "))
    Fibonacci_found_value = Fibonacci.Fibonacci_Search.FibonacciSearch(file_array, search_value)
    if Fibonacci_found_value is -1:
        print("There are no records with value '{}'".format(search_value))
    else:
        print("Found person with value matching to {}".format(search_value))
        print(file_array[Fibonacci_found_value].name,
              file_array[Fibonacci_found_value].salary,
              file_array[Fibonacci_found_value].position,
              file_array[Fibonacci_found_value].working_years,
              file_array[Fibonacci_found_value].kids, sep="\t\t")
