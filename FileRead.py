import random
from time import sleep
from math import log, log10, log2, pow
from os import path
from src.FileClass.FileClass import File
from src.SomeHelpingDefs import LittleHelpDefs as Helpful
from src.ThirdLab.LinkedList.LinkedList import LinkedList
from src.ThirdLab.LinkedList.DoubleLinkedList import LinkedList as DoubleLinkedList
from src.ThirdLab.LinkedList.CircularLinkedList import CircularLinkedList
from src.ThirdLab.Stack.Stack import Stack
from src.ThirdLab.Queue.Queue import Queue
from src.SearchAlgorithms.BST import BST


def first_lab(unsorted_file_array: list, sorted_file_array: list):
    """
    Method which represents first lab
    :param unsorted_file_array: The unsorted array of instances of File class
    :param sorted_file_array: The sorted array of instances of File class
    :return:
    """
    print(Helpful.colored("\t\t.....LAB 1.....", "green"))
    search_value = int(input("Enter Amount of Salary to Search --> "))

    Helpful.printing_output(
        name="Fibonacci",
        array=sorted_file_array,
        index=Helpful.FibS.fibonacci_search(
            lys=sorted_file_array,
            val=search_value)[0],
        search_value=search_value
    )

    Helpful.printing_output(
        name="Secventional",
        array=sorted_file_array,
        index=Helpful.SecvS.Secventional_Search(
            array=sorted_file_array,
            value=search_value)[0],
        search_value=search_value
    )

    Helpful.printing_output(
        name="Binary",
        array=sorted_file_array,
        index=Helpful.BinS.binary_search(
            sorted_collection=sorted_file_array,
            item=search_value)[0],
        search_value=search_value
    )

    Helpful.printing_output(
        name="Interpolation",
        array=sorted_file_array,
        index=Helpful.InterpS.interpolation_search(
            sorted_collection=sorted_file_array,
            item=search_value
        )[0],
        search_value=search_value
    )

    bst_balanced_tree = Helpful.BST.buildBalancedTree(
        sortedList=sorted_file_array.copy(),
        start=0,
        end=len(sorted_file_array)
    )
    bst_search_result = Helpful.BST.BinaryTree.lookup(bst_balanced_tree, search_value)
    Helpful.bst_output_print("BST", bst_search_result, search_value)
    Helpful.BST.loop_counter = 0

    # Printing step counter for each algorithm with random search position

    print(Helpful.colored("\nStep counter for each algorithm with random search position", "cyan"))
    random_element = random.randint(0, len(sorted_file_array) - 1)
    print(sorted_file_array[random_element].name, sorted_file_array[random_element].salary, sep="\t")
    print("\tRandom position is " + Helpful.colored("{}".format(str(random_element)), "red") + ", with value ==> " +
          Helpful.colored("{}".format(
              str(sorted_file_array[random_element].salary)
          ),
              "yellow"
          ))

    print(Helpful.colored("\t\tFibonacci algorithm steps: ", "magenta") +
          str(Helpful.FibS.fibonacci_search(
              lys=sorted_file_array,
              val=sorted_file_array[random_element].salary)[1]
              )
          )

    print(Helpful.colored("\t\tSecventional algorithm steps: ", "magenta") +
          str(Helpful.SecvS.Secventional_Search(
              array=sorted_file_array,
              value=sorted_file_array[random_element].salary)[1]
              )
          )

    print(Helpful.colored("\t\tBinary algorithm steps: ", "magenta") +
          str(Helpful.BinS.binary_search(
              sorted_collection=sorted_file_array,
              item=sorted_file_array[random_element].salary)[1]
              )
          )

    print(Helpful.colored("\t\tInterpolation algorithm steps: ", "magenta") +
          str(Helpful.InterpS.interpolation_search(
              sorted_collection=sorted_file_array,
              item=sorted_file_array[random_element].salary)[1]
              )
          )

    Helpful.BST.BinaryTree.lookup(
        self=bst_balanced_tree,
        value=sorted_file_array[random_element].salary
    )
    print(Helpful.colored("\t\tBST algorithm steps: ", "magenta") +
          str(Helpful.BST.get_loop_counter()))

    # Printing algorithms complexity

    algorithms_complexity = Helpful.algorithms_complexity(
        obj_array=sorted_file_array,
        bst_balanced_tree=bst_balanced_tree
    )
    print(
        Helpful.colored("\nPractical Complexity of Algorithms:", "cyan") +
        Helpful.colored("\n\tSecventional search algorithm: ", "magenta") + str(algorithms_complexity[0]) +
        Helpful.colored("\n\tInterpolation search algorithm: ", "magenta") + str(algorithms_complexity[1]) +
        Helpful.colored("\n\tBinary search algorithm: ", "magenta") + str(algorithms_complexity[2]) +
        Helpful.colored("\n\tFibonacci search algorithm: ", "magenta") + str(algorithms_complexity[3]) +
        Helpful.colored("\n\tBST search algorithm: ", "magenta") + str(algorithms_complexity[4])
    )

    print(
        Helpful.colored("\nTheoretic Complexity of Algorithms:", "cyan") +
        Helpful.colored("\n\tSecventional search algorithm: ", "magenta") +
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


def second_lab(unsorted_file_array: list, sorted_file_array: list):
    """
    Method which represents second lab
    :param unsorted_file_array: The unsorted array of instances of File class
    :param sorted_file_array: The sorted array of instances of File class
    :return:
    """

    print(Helpful.colored("\n\t\t..... LAB 2 .....", "green") +
          Helpful.colored("\nStep counter for each sorting algorithm/ Practical complexity", "cyan")
          )

    print(Helpful.colored("\tBubble_sort loop counter: ", "magenta"),
          Helpful.BubbleS.bubble_sort(
              collection=unsorted_file_array.copy())[1]
          )

    print(Helpful.colored("\tInsertion_sort loop counter: ", "magenta"),
          Helpful.InsS.insertion_sort(
              collection=unsorted_file_array.copy())[1]
          )

    Helpful.SelS.selection_sort(
        collection=unsorted_file_array.copy()
    )
    print(Helpful.colored("\tSelection_sort loop counter: ", "magenta"),
          Helpful.SelS.get_loop_counter())

    print(Helpful.colored("\tQuick_sort loop counter: ", "magenta"),
          Helpful.QuickS.quick_sort_3partition(
              sorting=unsorted_file_array.copy(),
              left=0,
              right=len(unsorted_file_array.copy()) - 1,
              check=0,
              loop_count=0
          )[1]
          )

    Helpful.ShellS.shell_sort(
        collection=unsorted_file_array.copy()
    )
    print(Helpful.colored("\tShell_sort loop counter: ", "magenta"),
          Helpful.ShellS.get_loop_counter())

    Helpful.HeapS.heap_sort(
        unsorted=unsorted_file_array.copy()
    )
    print(Helpful.colored("\tHeap_sort loop counter: ", "magenta"),
          Helpful.HeapS.get_loop_counter())

    Helpful.MergeS.merge_sort(
        collection=unsorted_file_array.copy()
    )
    print(Helpful.colored("\tMerge_sort loop counter: ", "magenta"),
          Helpful.MergeS.get_loop_counter())

    print(
        Helpful.colored("\nTheoretic Complexity of Algorithms:", "cyan") +
        Helpful.colored("\n\tBubble sort algorithm: ", "magenta") +
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


def third_lab(unsorted_file_array: list, sorted_file_array: list):
    """
    Method which represents the third lab
    :param unsorted_file_array: The unsorted array of instances of File class
    :param sorted_file_array: The sorted array of instances of File class
    :return:
    """
    print("\t\t.....LAB 3.....")

    def linked_l():
        """
        Method for operating with Linked List
        :return:
        """

        def ll_print(ll: LinkedList):
            """
            Method for printing Linked List
            :param ll: Linked List
            """

            ll.print_list()
            print("Linked list Data End")

        linked_list = LinkedList()
        for ll_item in sorted_file_array:
            linked_list.insert_tail(ll_item)
        ll_print(linked_list)
        linked_list.search(int(input("Input salary to search ->")))
        sleep(10)
        print("\nDelete Head")
        linked_list.delete_head()
        ll_print(linked_list)
        sleep(10)
        print("\nDelete Tail")
        linked_list.delete_tail()
        ll_print(linked_list)
        print("Linked List End\n")

    def double_ll():
        """
        Method for operating with Double Linked List
        :return:
        """

        def dll_print(dll: DoubleLinkedList):
            """
            Printing Double Linked List
            :param dll: Double Linked List object
            :return:
            """
            dll.display()
            print("End Double_LL Data")

        double_linked_list = DoubleLinkedList()
        double_linked_list.insertHead(sorted_file_array[0])
        for index, dll_item in enumerate(sorted_file_array):
            if index != 0:
                double_linked_list.insertTail(dll_item)
        dll_print(double_linked_list)
        double_linked_list.search(int(input("Input salary to search ->")))

        print("\nDelete Head")
        double_linked_list.deleteHead()
        dll_print(double_linked_list)
        sleep(10)
        print("\nDelete Tail")
        double_linked_list.deleteTail()
        dll_print(double_linked_list)
        sleep(10)
        print("\nDelete item by index")
        double_linked_list.delete(int(input("Input an item index to delete ->")))
        dll_print(double_linked_list)
        print("End Of Double-Linked-List\n")

    def circular_ll():
        """
        Method for operating with Circular Linked List
        :return:
        """

        def circular_print(cll: CircularLinkedList):
            """
            Method for printing Circular Linked List
            :param cll: instance of CircularLinkedList class
            :return:
            """

            cll.print()
            print("END Circular_LL Data")

        circular_linked_list = CircularLinkedList()
        for cll_item in sorted_file_array:
            circular_linked_list.append(cll_item)

        circular_print(circular_linked_list)
        circular_linked_list.search_for_element(int(input("Input salary to search ->")))
        sleep(10)
        print("\nDelete Rear")
        circular_linked_list.delete_rear()
        circular_print(circular_linked_list)
        sleep(10)
        print("\nDelete Front")
        circular_linked_list.delete_front()
        circular_print(circular_linked_list)
        print("End Of Circular-Linked-List\n")

    def stack():
        """
        Method for operating with Stack
        :return:
        """

        def stack_print(st: Stack):
            """
            Method for printing Stack
            :param st: instance of Stack class
            :return:
            """
            st.print()
            print("End Stack Data")

        stack_obj = Stack(
            limit=len(sorted_file_array)
        )
        for stack_item in sorted_file_array:
            stack_obj.push(stack_item)
        stack_print(stack_obj)
        print("\nStack Pop")
        stack_obj.pop()
        stack_print(stack_obj)
        sleep(10)
        stack_obj.search(int(input("Input salary to search --> ")))
        sleep(10)
        print("\nDelete item value")
        stack_obj.delete_item(int(input("Input salary to delete --> ")))
        sleep(10)
        stack_print(stack_obj)
        print("End of Stack \n")

    def queue():
        def queue_print(qe):
            qe.print()
            print("End Queue Data")

        print("Queue")
        queue_obj = Queue()
        for qe_item in sorted_file_array:
            queue_obj.put(qe_item)
        queue_print(queue_obj)
        get_item = queue_obj.get()
        get_item.print_data()
        queue_print(queue_obj)
        print("\nSearch by value")
        queue_obj.search(int(input("Input salary to search --> ")))
        print("End Of Queue")

    def bst():
        """
        Method to operate with BST
        :return:
        """

        def bst_output_print(name,
                             item,
                             search_value
                             ):

            print("\n{} search result: ".format(name))
            if item is None:
                print("\tThere are no records with value {} ".format(search_value))
            else:
                print("\tFound person with value matching to {} ".format(search_value))
                print("\t" + item.value.name,
                      item.value.salary,
                      item.value.position,
                      item.value.working_years,
                      item.value.kids, sep="\t\t")

        def print_bst(bst_bt: BST):
            """
            Method to print BST structure
            :param bst_bt:
            :return:
            """
            bst_bt.print_tree()
            print("End of BST Data")

        bst_balanced_tree = BST.buildBalancedTree(sorted_file_array.copy(), 0, len(sorted_file_array))
        print_bst(bst_balanced_tree)
        bst_balanced_tree.delete(int(input("Input salary to search --> ")))
        print_bst(bst_balanced_tree)
        bst_search_result = BST.BinaryTree.lookup(bst_balanced_tree, int(input("Input salary to search --> ")))
        bst_output_print("BST", bst_search_result, int(input("Input salary to search --> ")))
        print("End Of BST")

    while True:
        choose = int(
            input(
                "\nChoose what to display:"
                "\n\t1 -> Linked-List"
                "\n\t2 -> Double-Linked-List"
                "\n\t3 -> Circular-Linked-List"
                "\n\t4 -> Stack"
                "\n\t5 -> Queue"
                "\n\t6 -> BST"
                "\n\t7 -> Exit"
                "\n\t--------> "
            )
        )
        third_lab_methods = {
            1: linked_l,
            2: double_ll,
            3: circular_ll,
            4: stack,
            5: queue,
            6: bst
        }
        if 1 <= choose <= 6:
            third_lab_methods.get(choose)()
        elif choose == 7:
            break
        else:
            print("!!!Incorrect input!!!")
            continue


def main():
    with open("{}/Result".format(path.abspath('ResultTableFiles')), "r") as file:
        data = file.readlines()

    unsorted_file_array = Helpful.parse_data_to_array_objects(data, File)
    sorted_file_array = Helpful.sorted_table_file_creator(unsorted_file_array.copy())

    labs = {
        1: first_lab,
        2: second_lab,
        3: third_lab,
        5: exit
    }
    lab_choose = int(
        input(
            "Choose what lab to display:"
            "\n\t1 --> First Lab"
            "\n\t2 --> Second Lab"
            "\n\t3 --> Third Lab"
            "\n\t5 --> Exit"
            "\n\t ----> "
        )
    )
    if lab_choose != 5:
        labs.get(lab_choose, "Invalid lab")(unsorted_file_array, sorted_file_array)
    elif lab_choose == 5:
        labs.get(lab_choose)(0)


if __name__ == '__main__':
    main()
