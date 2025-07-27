class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove node from the list."""
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_front(self, node):
        """Add node right after head (most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self._add_to_front(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            # Remove from tail
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

"""
Your implementation of an LRU (Least Recently Used) Cache using a hashmap + doubly linked list is excellent — 
it's clean, efficient, and uses the right data structures to ensure O(1) time complexity for both get() and put() operations.
Here’s a quick breakdown and a few notes to reinforce understanding:
✅ Core Concepts
Hashmap (self.cache):
Maps keys to their corresponding nodes (for O(1) access to the node).

Doubly Linked List:
Maintains usage order: most recently used at the front, least recently used at the back.
Dummy head and tail nodes simplify insertions and deletions.
_remove() and _add_to_front():
_remove: unlinks a node from the list.
_add_to_front: adds a node right after the head (marks it as most recently used).

Eviction:
When cache exceeds capacity, remove the node just before tail (the least recently used node).
🔁 get() Operation:
If the key exists:
Move the accessed node to the front (MRU).
Return its value.
Otherwise, return -1.

✍️ put() Operation:
If key exists:
Remove the old node (you’ll replace it).
Create and add a new node at the front.
Insert in the hashmap.
If size exceeds capacity:
Remove the LRU node (before tail) and delete it from hashmap.

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))   # Returns 1
cache.put(3, 3)       # Evicts key 2
print(cache.get(2))   # Returns -1 (not found)
cache.put(4, 4)       # Evicts key 1
print(cache.get(1))   # Returns -1 (not found)
print(cache.get(3))   # Returns 3
print(cache.get(4))   # Returns 4




"""