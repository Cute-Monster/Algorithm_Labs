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
    print("\n{} search result:".format(name))
    if index is -1:
        print("\tThere are no records with value '{}' ".format(search_value))
    else:
        print("\tFound person with value matching to {} at #{}".format(search_value, index))
        print("\t" + array[index].name,
              array[index].salary,
              array[index].position,
              array[index].working_years,
              array[index].kids, sep="\t\t")
