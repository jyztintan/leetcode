class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.least_recent = Node(0,0)
        self.most_recent = Node(0, 0)
        self.least_recent.next = self.most_recent
        self.most_recent.prev = self.least_recent

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        node.prev = self.most_recent.prev
        node.next = self.most_recent
        self.most_recent.prev.next = node
        self.most_recent.prev = node


    def get(self, key: int) -> int:

        if key in self.d:
            node = self.d[key]
            self.remove(node)
            self.add(node)
            return node.value

        return -1

    def put(self, key: int, value: int):

        if key in self.d:
            self.remove(self.d[key])

        elif len(self.d) == self.capacity:
            least_recent = self.least_recent.next
            self.remove(least_recent)
            self.d.pop(least_recent.key)
            
        new_node = Node(key, value)
        self.add(new_node)
        self.d[key] = new_node

# cache = LRUCache(2)
# cache.put(1,1)
# cache.put(2,2)
# print(cache.get(1))
# cache.put(3,3)
# print(cache.get(2))