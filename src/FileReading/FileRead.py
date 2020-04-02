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

import random
from math import log, log10, log2, pow
from os import path
from src.FileClass.FileClass import File
from src.SomeHelpingDefs import LittleHelpDefs as Helpful
import src.ThirdLab.LinkedList.LinkedList as LinkedList
import src.ThirdLab.LinkedList.DoubleLinkedList as DLL
import src.ThirdLab.LinkedList.CircularLinkedList as Circular
import src.ThirdLab.Stack.Stack as Stack
import src.ThirdLab.Queue.Queue as Queue
import src.SearchAlgorithms.BST.BST as BST


def main():
    with open("{}/Result".format(path.abspath('../ResultTableFiles')), "r") as file:
        data = file.readlines()

    unsorted_file_array = Helpful.parse_data_to_array_objects(data, File)
    sorted_file_array = Helpful.sorted_table_file_creator(unsorted_file_array.copy())

    def first_lab():
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

        bst_balanced_tree = Helpful.BST.buildBalancedTree(sorted_file_array.copy(), 0, len(sorted_file_array))
        bst_search_result = Helpful.BST.binaryTree.lookup(bst_balanced_tree, search_value)
        Helpful.bst_output_print("BST", bst_search_result, search_value)
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

        Helpful.BST.binaryTree.lookup(bst_balanced_tree, sorted_file_array[random_element].salary)
        print(Helpful.colored("\t\tBST algorithm steps: ", "magenta") +
              str(Helpful.BST.get_loop_counter()))

        # Printing algorithms complexity

        algorithms_complexity = Helpful.algorithms_complexity(
            obj_array=sorted_file_array,
            bst_balanced_tree=bst_balanced_tree
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

    def second_lab():
        print(Helpful.colored("\n\t\t..... LAB 2 .....", "green"))
        print(Helpful.colored("Step counter for each sorting algorithm/ Practical complexity", "cyan"))
        # unsorted_file_array.sort(key=lambda x: x.salary, reverse=True)
        bubble_sorted = Helpful.BubbleS.bubble_sort(unsorted_file_array.copy())
        print(Helpful.colored("\tBubble_sort loop counter: ", "magenta"),
              bubble_sorted[1])

        insertion_sorted = Helpful.InsS.insertion_sort(unsorted_file_array.copy())
        print(Helpful.colored("\tInsertion_sort loop counter: ", "magenta"),
              insertion_sorted[1])

        selection_sorted = Helpful.SelS.selection_sort(unsorted_file_array.copy())
        print(Helpful.colored("\tSelection_sort loop counter: ", "magenta"),
              Helpful.SelS.get_loop_counter())

        quick_sorted = Helpful.QuickS.quick_sort_3partition(
            unsorted_file_array.copy(),
            0,
            len(unsorted_file_array.copy()) - 1,
            0,
            0
        )
        print(Helpful.colored("\tQuick_sort loop counter: ", "magenta"),
              quick_sorted[1])

        shell_sorted = Helpful.ShellS.shell_sort(unsorted_file_array.copy())
        print(Helpful.colored("\tShell_sort loop counter: ", "magenta"),
              Helpful.ShellS.get_loop_counter())

        heap_sorted = Helpful.HeapS.heap_sort(unsorted_file_array.copy())
        print(Helpful.colored("\tHeap_sort loop counter: ", "magenta"),
              Helpful.HeapS.get_loop_counter())

        merge_sorted = Helpful.MergeS.merge_sort(unsorted_file_array.copy())
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

    def third_lab():
        print("\t\t.....LAB 3.....")

        def linked_l():
            def ll_print(ll):
                ll.print_list()
                print("Linked list Data End")

            linked_list = LinkedList.LinkedList()
            for ll_item in sorted_file_array:
                linked_list.insert_tail(ll_item)
            ll_print(linked_list)
            linked_list.search(int(input("Input salary to search ->")))
            input()
            print("\nDelete Head")
            linked_list.delete_head()
            ll_print(linked_list)
            input()
            print("\nDelete Tail")
            linked_list.delete_tail()
            ll_print(linked_list)
            print("Linked List End\n")

        def double_ll():
            def dll_print(dll):
                dll.display()
                print("End Double_LL Data")

            double_linked_list = DLL.LinkedList()
            double_linked_list.insertHead(sorted_file_array[0])
            for index, dll_item in enumerate(sorted_file_array):
                if index != 0:
                    double_linked_list.insertTail(dll_item)
            dll_print(double_linked_list)
            double_linked_list.search(int(input("Input salary to search ->")))
            input()
            print("\nDelete Head")
            double_linked_list.deleteHead()
            dll_print(double_linked_list)
            input()
            print("\nDelete Tail")
            double_linked_list.deleteTail()
            dll_print(double_linked_list)
            input()
            print("\nDelete item by index")
            double_linked_list.delete(int(input("Input an item index to delete ->")))
            dll_print(double_linked_list)
            print("End Of Double-Linked-List\n")

        def circular_ll():
            def circular_print(cll):
                cll.print()
                print("END Circular_LL Data")

            circular_linked_list = Circular.CircularLinkedList()
            for cll_item in sorted_file_array:
                circular_linked_list.append(cll_item)

            circular_print(circular_linked_list)
            circular_linked_list.search_for_element(int(input("Input salary to search ->")))
            print("\nDelete Rear")
            circular_linked_list.delete_rear()
            circular_print(circular_linked_list)
            print("\nDelete Front")
            circular_linked_list.delete_front()
            circular_print(circular_linked_list)
            print("End Of Circular-Linked-List\n")

        def stack():
            def stack_print(st):
                st.print()

            stack_obj = Stack.Stack(
                limit=len(sorted_file_array)
            )
            for stack_item in sorted_file_array:
                stack_obj.push(stack_item)
            stack_print(stack_obj)
            print("\nStack Pop")
            stack_obj.pop()
            stack_print(stack_obj)
            stack_obj.search(int(input("Input salary to search --> ")))
            print("\nDelete item value")
            stack_obj.delete_item(int(input("Input salary to delete --> ")))
            stack_print(stack_obj)
            print("End of Stack \n")

        def queue():
            def queue_print(qe):
                qe.print()
                print("End Queue Data")

            print("Queue")
            queue_obj = Queue.Queue()
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
            def bst_output_print(name, item, search_value):
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

            def print_bst(bst_bt):
                bst_bt.print_tree()
                print("End of BST Data")

            bst_balanced_tree = BST.buildBalancedTree(sorted_file_array.copy(), 0, len(sorted_file_array))
            print_bst(bst_balanced_tree)
            bst_balanced_tree.delete(int(input("Input salary to search --> ")))
            print_bst(bst_balanced_tree)
            bst_search_result = BST.binaryTree.lookup(bst_balanced_tree, int(input("Input salary to search --> ")))
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

            if choose == 1:
                linked_l()
            elif choose == 2:
                double_ll()
            elif choose == 3:
                circular_ll()
            elif choose == 4:
                stack()
            elif choose == 5:
                queue()
            elif choose == 6:
                bst()
            elif choose == 7:
                break
            else:
                print("!!!Incorrect input!!!")
                continue

    def four_lab():
        print("\t\t.....LAB 4.....")

    labs = {
        '1': first_lab,
        '2': second_lab,
        '3': third_lab,
        '4': four_lab,
        '5': exit
    }

    def labs_return():
        lab_choose = input(
            "Choose what lab to display:"
            "\n\t1 --> First Lab"
            "\n\t2 --> Second Lab"
            "\n\t3 --> Third Lab"
            "\n\t4 --> Four Lab"
            "\n\t5 --> Exit"
            "\n\t ----> "
        )
        return labs.get(lab_choose, "Invalid lab")()

    while True:
        labs_return()


if __name__ == '__main__':
    main()
