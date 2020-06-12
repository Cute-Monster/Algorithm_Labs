loop_counter = 0


class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None

    def setLeftBranch(self, node):
        self.leftBranch = node

    def setRightBranch(self, node):
        self.rightBranch = node

    def setParent(self, parent):
        self.parent = parent

    def getValue(self):
        return self.value

    def getLeftBranch(self):
        return self.leftBranch

    def getRightBranch(self):
        return self.rightBranch

    def getParent(self):
        return self.parent

    def insert(self, value):
        """
        Insert new node with data key set to value
        Return inserted node object to caller, or None if node not inserted (when node was already present)
        """
        if value < self.value.salary:
            if self.getLeftBranch() is None:
                self.setLeftBranch(BinaryTree(value))
                self.getLeftBranch().setParent(self)
                return self.getLeftBranch()
            else:
                return self.getLeftBranch().insert(value)
        elif value > self.value.salary:
            if self.getRightBranch() is None:
                self.setRightBranch(BinaryTree(value))
                self.getRightBranch().setParent(self)
                return self.getRightBranch()
            else:
                return self.getRightBranch().insert(value)

    def lookup(self, value):
        """
        Lookup node containing data key set to value
        Returns node object to caller, or None if not found
        """
        global loop_counter
        loop_counter += 1
        if value < self.value.salary:
            loop_counter += 1
            if self.getLeftBranch() is None:
                return None
            return self.getLeftBranch().lookup(value)
        elif value > self.value.salary:
            loop_counter += 1
            if self.getRightBranch() is None:
                return None
            return self.getRightBranch().lookup(value)
        else:
            loop_counter += 1
            return self

    def delete(self, value):
        """
        Delete node containing data key set to value
        Returns status text message
        """
        # get node containing value and its number of children | or return with node not found message
        node = self.lookup(value)
        if not node:
            return "Error in delete method: node " + str(value) + " not found"
        else:
            children_count = node.children_count(node)
        if children_count == 0:
            # if node has no children, just remove it
            parent = node.getParent()
            if parent.getLeftBranch() is node:
                parent.setLeftBranch(None)
            else:
                parent.setRightBranch(None)
        elif children_count == 1:
            # if node has 1 child, replace node by its child
            if node.getLeftBranch():
                n = node.getLeftBranch()
            else:
                n = node.getRightBranch()
            parent = node.getParent()
            if parent:
                if parent.getLeftBranch() is node:
                    parent.setLeftBranch(n)
                else:
                    parent.setRightBranch(n)
        elif children_count == 2:
            # if node has 2 children, find its successor
            parent = node
            successor = node.getRightBranch()
            while successor.getLeftBranch():
                parent = successor
                successor = successor.getLeftBranch()
            # replace node value by its successor value
            node.value = successor.value
            # fix successor's parent's child
            if parent.getLeftBranch() == successor:
                parent.setLeftBranch(successor.getRightBranch())
            else:
                parent.setRightBranch(successor.getRightBranch())
        child_message_frag = ("no children", "1 child", "2 children")
        return f"Node {str(value)} has {str(child_message_frag[children_count])} and was successfully deleted"

    def children_count(self, node):
        """
        Returns the number of children of a tree node object: 0, 1, 2
        """
        if node is None:
            return None
        cnt = 0
        if self.getLeftBranch():
            cnt += 1
        if self.getRightBranch():
            cnt += 1
        return cnt

    def print_tree(self):
        """
        Print tree content in order
        """
        print("Parent => ", self.getValue().salary)
        if self.getLeftBranch():
            print("LeftBranch => ", self.getLeftBranch().getValue().salary)
            self.getLeftBranch().print_tree()
        print("Parent2 => ", self.getValue().salary)
        if self.getRightBranch():
            print("RightBranch => ", self.getRightBranch().getValue().salary)
            self.getRightBranch().print_tree()

    def __str__(self):
        return str(self.value)


"""
A Manual Method to Instantiate a Tree
-------------------------------------
n5 = binaryTree(5)
n2 = binaryTree(2)
n1 = binaryTree(1)
n4 = binaryTree(4)
n8 = binaryTree(8)
n6 = binaryTree(6)
n7 = binaryTree(7)
n3 = binaryTree(3)
n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)
n4.setLeftBranch(n3)
n3.setParent(n4)
# define sketch tree and animate search parameters
root = n5
findValue = '7'
listForTree = None
"""


def get_loop_counter():
    global loop_counter
    counter, loop_counter = loop_counter, 0
    return counter


# Helper functions to instantiate a tree from a list
# --------------------------------------------------

def buildBalancedTree(sortedList, start, end):
    """
    Build a balanced binary search tree from a sorted linked list.
    This function uses class binaryTree, with methods:
        'getLeftBranch()', 'getRightBranch()' and optionally setParent().
    Input:
        sortedList: sorted list, any data structure with 'pop(0)' method,
            which removes and returns the leftmost element of the list. The
            easiest thing to do is to use a list for the sorted
            list.
        start: int, start index, on initial call set to 0
        end: int, on initial call should be set to len(sortedList)
    Output: 
        root node of type binaryTree if the supplied list has 2 or more values,
            or None.
            
    Note:
        The sortedList list is destroyed during the process.
    """
    if start >= end:
        return None
    middle = (start + end) // 2
    node = buildBalancedTree(sortedList, start, middle)
    root = BinaryTree(sortedList.pop(0))
    root.setLeftBranch(node)
    if root.getLeftBranch():
        root.getLeftBranch().setParent(root)
    root.setRightBranch(buildBalancedTree(sortedList, middle + 1, end))
    if root.getRightBranch():
        root.getRightBranch().setParent(root)
    return root


def buildUnbalancedTree(unsortedList, rootValue):
    """
    Build an unbalanced binary search tree
    Input: An unsorted list of key values to generate a tree, 
           The root key value, a member of the unsortedList.         
    Output: root_node when rootValue was found in unsortedList, otherwise return None.
                         
    Notes:
        The unsortedList list is destroyed during the process.
        The nodes will be inserted into the tree using unsortedList list from left to right,
            Uses the binaryTree.insert() method.
    """
    if rootValue not in unsortedList:
        return None
    root_index = unsortedList.index(rootValue)
    root_node = BinaryTree(unsortedList[root_index])
    unsortedList.remove(unsortedList[root_index])
    while len(unsortedList):
        root_node.insert(unsortedList[0])
        unsortedList.remove(unsortedList[0])
    return root_node
