class Node:
    """
        Creating a single node class with two cells one for data
        and other for reference link
    """
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    """
        A linked list class where all the nodes are added & deleted
        from the begining, end and middle.
    """
    def __init__(self):
        self.head = None

    # A print method that will print the status of the LL
    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "------>", end=" ")
                n = n.ref

    # This method will add the node to LL from the starting point/begining
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # This method will add the node to LL from the ending point.
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    # This method will add the node to LL in middle but after the choosen node
    def add_after(self,data,after):
        n = self.head
        while n is not None:
            if after==n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

LL1 = LinkedList()
LL1.add_end(100)
LL1.add_begin(20)
LL1.add_end(300)
LL1.add_after(200,100)
LL1.add_after(200,500)   # 500 is not present in LL so it will print node not present
LL1.print_LL()
