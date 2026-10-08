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
        while temp: # not temp.next unlike in pop
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

    def pop(self):
        if self.length == 0:
            return None
        if self.length > 0:
            temp = self.head
            pre = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value


my_list = linkedlist(4)  # Starts with [4]
my_list.append(5)        # Adds 5 -> [4, 5]
my_list.append(6)        # Adds 6 -> [4, 5, 6]

my_list.print_linkedlist()


my_list.pop()

my_list.print_linkedlist()