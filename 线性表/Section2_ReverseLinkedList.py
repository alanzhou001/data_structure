class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # 创建头结点
        self.head = Node()

    def length(self):
        current = self.head
        count = 0
        while current.next is not None:
            count += 1
            current = current.next
        return count

    def search(self, x):
        current = self.head.next
        position = 0
        while current is not None:
            if current.data == x:
                return position
            current = current.next
            position += 1
        return -1

    def insert(self, i, x):
        if i < 0 or i > self.length():
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(i):
            current = current.next
        new_node = Node(x)
        new_node.next = current.next
        current.next = new_node

    def remove(self, i):
        if i < 0 or i >= self.length():
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(i):
            current = current.next
        current.next = current.next.next

    def clear(self):
        self.head.next = None
        
    def traverse(self):
        #TODO
        return

    def reverse(self):
        #TODO
        return


a = LinkedList()
a.insert(0,3)
a.insert(0,2)
a.insert(0,1)
a.traverse()
a.reverse()
a.traverse()
