class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

class TwoDirectionalList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, data):
        if not self.head:
            n = Node(data)
            self.head = n
            self.tail = n
        else:
            n = self.tail
            new_node = Node(data)
            n.next = new_node
            new_node.prev = n
            self.tail = new_node

    def add_backgound(self, data):
        if not self.head:
            n = Node(data)
            self.head = n
            self.tail = n
        else:
            n = self.head
            new_node = Node(data)
            n.prev = new_node
            new_node.next = n
            self.head = new_node

    def add_position(self, data, position):
        if not self.head:
            n = Node(data)
            self.tail = n
            self.head = n
        elif position <= 1:
            n = self.head
            new_node = Node(data)
            n.prev = new_node
            new_node.next = n
            self.head = new_node
        else:
            n = self.head
            count = 2
            while n.next != None and position > count:
                n = n.next
                count += 1
            if position > count:
                new_node = Node(data)
                n.next = new_node
                new_node.prev = n
                self.tail = new_node
            else:
                new_node = Node(data)
                tmp = n.next
                n.next = new_node
                new_node.prev = n
                tmp.prev = new_node
                new_node.next = tmp

    def rm_front(self):
        n = self.tail
        self.tail.prev.next = None
        self.tail = n.prev

    def rm_background(self):
        n = self.head
        self.head.next.prev = None
        self.head = n.next

    def rm_position(self, position):
        n = self.head
        if position <= 1:
            self.head.next.prev = None
            self.head = n.next
        else:
            count = 1
            while n.next != None and position > count:
                n = n.next
                count += 1
            if position > count:
                tmp = n
                n.prev.next = None
                n = tmp.prev
            else:
                new_connect = n.prev
                new_connect2 =  n.next
                n.next.prev = None
                new_connect.next = new_connect2
                new_connect2.prev = new_connect

    def print_list(self):
        n = self.head
        while n:
            print(n)
            n = n.next

    def print_list2(self):
        n = self.tail
        while n:
            print(n)
            n = n.prev

ll = TwoDirectionalList()
ll.add_front("maciek")
ll.add_front("kamil")
ll.add_front("filip")
ll.add_front(2.31)
ll.add_backgound("pierwszy")
ll.rm_front()
ll.rm_background()
ll.add_backgound("kek")
ll.add_front("kek1")
ll.add_position("position", 3)
ll.print_list2()
ll.rm_position(3)
print("")
ll.print_list()