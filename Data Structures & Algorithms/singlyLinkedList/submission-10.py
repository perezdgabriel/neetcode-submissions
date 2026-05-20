class Node:
    def __init__(self, value: int, next: Node | None = None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"node({self.value}, {self.next})"

class LinkedList:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.value
            curr = curr.next
            i += 1
        return -1
            
    def insertHead(self, val: int) -> None:
        new = Node(val, self.head.next)
        self.head.next = new
        if not new.next:
            self.tail = new

    def insertTail(self, val: int) -> None:
        new = Node(val)
        self.tail.next = new
        self.tail = new

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while i < index and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True

        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        values = []
        while curr:
            values.append(curr.value)
            curr = curr.next
        return values
