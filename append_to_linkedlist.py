class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class linkedlist:
    def __init__(self,value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1

    def print_linkedlist(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

        self.length += 1
        return True


my_list = linkedlist(4)  # Starts with [4]
my_list.append(5)        # Adds 5 -> [4, 5]
my_list.append(6)        # Adds 6 -> [4, 5, 6]

my_list.print_linkedlist()# append method
