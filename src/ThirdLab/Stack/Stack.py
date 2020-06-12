class Stack:
    """ A stack is an abstract data type that serves as a collection of
    elements with two principal operations: push() and pop(). push() adds an
    element to the top of the stack, and pop() removes an element from the top
    of a stack. The order in which elements come off of a stack are
    Last In, First Out (LIFO).
    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """

    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def __bool__(self):
        return bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        """ Push an element to the top of the stack."""
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(data)

    def pop(self):
        """ Pop an element off of the top of the stack."""
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        """ Peek at the top-most element of the stack."""
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        """ Check if a stack is empty."""
        return not bool(self.stack)

    def size(self):
        """ Return the size of the stack."""
        return len(self.stack)

    def print(self):
        temp_array = []
        stack_copy = self.stack.copy()
        while len(stack_copy) != 0:
            temp_array.append(stack_copy.pop())
        temp_array.reverse()
        self.print_data(temp_array)

    def search(self, search_item):
        temp_array = []
        while not self.is_empty():
            item = self.pop()
            if item.salary == search_item:
                print("\t" + item.name,
                      item.salary,
                      item.position,
                      item.working_years,
                      item.kids, sep="\t\t")
            temp_array.append(item)
        temp_array.reverse()
        for item in temp_array:
            self.push(item)

    def delete_item(self, search_item):
        temp_array = []
        while not self.is_empty():
            item = self.pop()
            if item.salary == search_item:
                continue
            else:
                temp_array.append(item)
        temp_array.reverse()
        for item in temp_array:
            self.push(item)

    @staticmethod
    def print_data(array):
        for item in array:
            print("\t" + item.name,
                  item.salary,
                  item.position,
                  item.working_years,
                  item.kids, sep="\t\t")


class StackOverflowError(BaseException):
    pass


if __name__ == "__main__":
    stack = Stack()
    for i in range(10):
        stack.push(i)

    print("Stack demonstration:\n")
    stack.search(5)
    # print("Initial stack: " + str(stack))
    # print("pop(): " + str(stack.pop()))
    # print("After pop(), the stack is now: " + str(stack))
    # print("peek(): " + str(stack.peek()))
    # stack.push(100)
    # print("After push(100), the stack is now: " + str(stack))
    # print("is_empty(): " + str(stack.is_empty()))
    # print("size(): " + str(stack.size()))
