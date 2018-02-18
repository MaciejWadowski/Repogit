class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class List:
    def __init__(self):
        self.head = None

    def add(self, data):
        if not self.head:
            n = Node(data)
            self.head = n
        else:
            n = self.head
            while n.next != None:
                n = n.next
            new_node = Node(data)
            n.next = new_node

    def add_first(self, data):
        if not self.head:
            n = Node(data)
            self.head = n
        else:
            n = Node(data)
            n.next = self.head
            self.head = n

    def add_position(self, data, position):
        if not self.head:
            n = Node(data)
            self.head = n
        elif position == 1:
            n = Node(data)
            n.next = self.head
            self.head = n
        elif position < 1:
            print("List doesn't have negative position.")
        else:
            n = self.head
            count = 2
            new_node = Node(data)
            while n.next != None and position != count:
                n = n.next
                count += 1
            if position != count:
                n.next = new_node
            else:
                tmp = n.next
                n.next = new_node
                new_node.next = tmp


    def rm_first(self):
        self.head = self.head.next

    def rm_last(self):
        n = self.head
        while n.next.next != None:
            n = n.next
        n.next = None

    def rm_position(self, position):
        if position < 1:
            print("There is no such a position.")
        elif position == 1:
            self.head = self.head.next
        else:
            count = 2
            n = self.head
            while n.next.next != None and position > count:
                n = n.next
                count += 1
            n.next = n.next.next


    def print_list(self):
        n = self.head
        while n:
            print(n)
            n = n.next

ll = List()
ll.add("maciek")
ll.add("XD")
ll.add(14)
ll.add("lmaooo")
ll.add("mackooo")
ll.rm_first()
ll.rm_first()
ll.rm_last()
ll.add(True)
ll.add(2.34)
ll.add_first(2.22)
ll.add_position("xd", 4)
ll.rm_position(2)
ll.add("smth")
ll.print_list()