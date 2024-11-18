class Node:
    def __init__(self, freq):
        self.freq = freq
        self.next = None
        self.prev = None
        self.keys = set()

class Node:
    def __init__(self, freq):
        self.freq = freq
        self.prev = None
        self.next = None
        self.keys = set()


class AllOne:
    def __init__(self):
        self.head = Node(0)  # Dummy head
        self.tail = Node(0)  # Dummy tail
        self.head.next = self.tail  # Link dummy head to dummy tail
        self.tail.prev = self.head  # Link dummy tail to dummy head
        self.map = {}  # Mapping from key to its node

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            freq = node.freq
            node.keys.remove(key)  # Remove key from current node

            nextNode = node.next
            if nextNode == self.tail or nextNode.freq != freq + 1:
                # Create a new node if next node does not exist or freq is not freq + 1
                newNode = Node(freq + 1)
                newNode.keys.add(key)
                newNode.prev = node
                newNode.next = nextNode
                node.next = newNode
                nextNode.prev = newNode
                self.map[key] = newNode
            else:
                # Increment the existing next node
                nextNode.keys.add(key)
                self.map[key] = nextNode

            # Remove the current node if it has no keys left
            if not node.keys:
                self.removeNode(node)
        else:  # Key does not exist
            firstNode = self.head.next
            if firstNode == self.tail or firstNode.freq > 1:
                # Create a new node
                newNode = Node(1)
                newNode.keys.add(key)
                newNode.prev = self.head
                newNode.next = firstNode
                self.head.next = newNode
                firstNode.prev = newNode
                self.map[key] = newNode
            else:
                firstNode.keys.add(key)
                self.map[key] = firstNode

    def dec(self, key: str) -> None:
        if key not in self.map:
            return  # Key does not exist

        node = self.map[key]
        node.keys.remove(key)
        freq = node.freq

        if freq == 1:
            # Remove the key from the map if freq is 1
            del self.map[key]
        else:
            prevNode = node.prev
            if prevNode == self.head or prevNode.freq != freq - 1:
                # Create a new node if the previous node does not exist or freq is not freq - 1
                newNode = Node(freq - 1)
                newNode.keys.add(key)
                newNode.prev = prevNode
                newNode.next = node
                prevNode.next = newNode
                node.prev = newNode
                self.map[key] = newNode
            else:
                # Decrement the existing previous node
                prevNode.keys.add(key)
                self.map[key] = prevNode

        # Remove the node if it has no keys left
        if not node.keys:
            self.removeNode(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""  # No keys exist
        return next(
            iter(self.tail.prev.keys)
        )  # Return one of the keys from the tail's previous node

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""  # No keys exist
        return next(
            iter(self.head.next.keys)
        )  # Return one of the keys from the head's next node

    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode  # Link previous node to next node
        nextNode.prev = prevNode  # Link next node to previous node

class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {}  # (key: str, node: Node)

    def inc(self, key: str) -> None:
        # Get current count
        if key in self.key_to_node:
            old_node = self.key_to_node[key]
            curr = old_node.freq
            # If the key had a count, we remove from our counts dictionary first
            old_node.keys.remove(key)
            if old_node.next == self.tail or old_node.next.freq != curr + 1:
                new_node = Node(curr + 1)
                new_node.keys.add(key)
                new_node.next = old_node.next
                old_node.next.prev = new_node
                new_node.prev = old_node
                old_node.next = new_node
            else:
                new_node = old_node.next
            self.key_to_node[key] = new_node

            if not old_node.keys:
                old_node.prev.next = old_node.next
                old_node.next.prev = old_node.prev

        else:
            if self.head.next == self.tail or self.head.next.freq > 1:
                new_node = Node(1)
                new_node.keys.add(key)
                new_node.next = self.head.next
                self.head.next.prev = new_node
                new_node.prev = self.head
                self.head.next = new_node
            else:
                new_node = self.head.next
                new_node.keys.add(key)
            self.key_to_node[key] = new_node

    def dec(self, key: str) -> None:
        # Remove key from curr count node
        old_node = self.key_to_node[key]
        curr = old_node.freq
        old_node.keys.remove(key)

        # If count becomes 0, delete. Otherwise add back to respective Node
        if curr - 1 == 0:
            del self.key_to_node[key]
        else:
            if old_node.prev == self.head or old_node.prev.freq != curr - 1:
                new_node = Node(curr - 1)
                new_node.next = old_node
                new_node.prev = old_node.prev
                old_node.prev.next = new_node
                old_node.prev = new_node
            else:
                new_node = old_node.prev
            new_node.keys.add(key)
            self.key_to_node[key] = new_node

        if not old_node.keys:
            old_node.prev.next = old_node.next
            old_node.next.prev = old_node.prev

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))


    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

# Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc("hello")
obj.dec("hello")
print(obj.getMaxKey())
print(obj.getMinKey())
obj.inc("leet")
print(obj.getMaxKey())
print(obj.getMinKey())
