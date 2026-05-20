class LinkedNode: 
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"LN({self.value}, {self.next})"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        if not self.head:
            return -1

        i = 0
        node = self.head
        while i <= index:
            if i == index:
                print(f'get {node}')
                return node.value if node else -1
            elif node == self.tail:
                return -1

            node = node.next
            i += 1
        
        return -1
       

    def insertHead(self, val: int) -> None:
        node = LinkedNode(val)
        node.next = self.head if self.head else None
        self.head = node
        if not self.tail:
            self.tail = node
        print(f"Insert head: {self.head}")

    def insertTail(self, val: int) -> None:
        node = LinkedNode(val)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node
        elif not self.head.next:
            self.head.next = node
        print(f"Insert Tail: {self.tail}, head: {self.head}")

    def remove(self, index: int) -> bool:
        node = self.head
        i=0
        if index == 0 and self.head:
            self.head = self.head.next
            return True

        while i < index and node.next:
            if i == index - 1:
                node.next = node.next.next
                return True
            elif node == self.tail:
                return False

            node = node.next
            i += 1

        return False

    def getValues(self) -> List[int]:
        values = []
        node = self.head
        print(f"head: {node}")
        while node is not None:
            print(f"Value: {node}")
            values.append(node.value)
            node = node.next
        return values