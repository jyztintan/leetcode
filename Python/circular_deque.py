class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.k = k
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.k == self.count:
            return False
        self.count += 1

        node = Node(value)
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        return True

    def insertLast(self, value: int) -> bool:
        if self.k == self.count:
            return False
        self.count += 1

        node = Node(value)
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        return True

    def deleteFront(self) -> bool:
        if self.count == 0:
            return False
        self.count -= 1

        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return True

    def deleteLast(self) -> bool:
        if self.count == 0:
            return False
        self.count -= 1

        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        return True

    def getFront(self) -> int:
        if self.count == 0:
            return -1
        return self.head.next.val

    def getRear(self) -> int:
        if self.count == 0:
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()