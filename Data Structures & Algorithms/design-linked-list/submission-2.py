class ListNode:
    def __init__(self, val: int, prev: ListNode | None = None, next: ListNode | None = None):
        self.val = val
        self.prev = prev
        self.next = next
    def __repr__(self):
        return f"n(v={self.val}, n={self.next})"


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head        

    def get(self, index: int) -> int:
        curr = self.head.next 
        i=0
        while curr and curr.next:
            if i == index:
                return curr.val
            i+=1
            curr = curr.next
        return -1

    def addAtHead(self, val: int) -> None:
        prev, next = self.head, self.head.next
        new = ListNode(val, prev=prev, next=next)
        prev.next = new
        next.prev = new
        print(self.head.next)

    def addAtTail(self, val: int) -> None:
        prev, next = self.tail.prev, self.tail
        new = ListNode(val, prev=prev, next=next)
        prev.next = new
        next.prev = new
        print(self.head.next)


    def addAtIndex(self, index: int, val: int) -> None:
        new = ListNode(val)
        curr = self.head
        i = -1
        while i < index and curr.next:
            curr = curr.next
            i+=1

        if i == index:
            prev= curr.prev
            new.next = curr
            new.prev = prev
            prev.next = new
            curr.prev = new
        print(f"atindex: {index}, i={i}, {self.head.next}")

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        i = 0
        while curr and curr.next:
            if i == index:
                prev, next = curr.prev, curr.next
                prev.next = next
                next.prev = prev
                break
            curr = curr.next
            i+=1

        
        print(self.head.next)




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)