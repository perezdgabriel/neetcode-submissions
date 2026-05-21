class Node:
    def __init__(self, value: int, prev: Node | None = None, next: Node | None = None):
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"node({self.value}, {self.next})"

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next.next is None

    def append(self, value: int) -> None:
        prev, next = self.tail.prev, self.tail
        new = Node(value)
        new.prev = prev
        new.next = next
        prev.next = new
        next.prev = new

    def appendleft(self, value: int) -> None:
        prev, next = self.head, self.head.next
        new = Node(value)
        new.prev = prev
        new.next = next
        prev.next = new
        next.prev = new

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last = self.tail.prev
        prev, next = last.prev, last.next
        prev.next = next
        next.prev = prev
        return last.value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first = self.head.next
        prev, next = first.prev, first.next
        prev.next = next
        next.prev = prev
        return first.value
        
