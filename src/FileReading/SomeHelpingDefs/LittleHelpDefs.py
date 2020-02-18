from termcolor import colored


def parse_data_to_array_objects(data, File):
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
    return array


def sorted_table_file(file, array):
    # file = open("../../ResultTableFiles/SortedFiles/SortedBySalary.txt", "w")
    array.sort(key=lambda x: x.salary, reverse=False)
    for item in array:
        file.writelines("{}\t\t{}\t\t{}\t\t{}\t\t{}\n".format(item.name, str(item.salary), item.position,
                                                              str(item.working_years), str(item.kids)))
    file.close()
    return array


def printing_output(name, array, index, search_value):
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
