class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = None
        node.prev = None
    
    def insert(self,node):
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev = node
        node.prev.next = node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        node = Node(key,value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache)>self.capacity:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
