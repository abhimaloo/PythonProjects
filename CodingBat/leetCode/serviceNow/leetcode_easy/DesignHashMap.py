class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

"""
You use a simple singly linked list (ListNode) to store entries within each bucket
 of your hash map (to handle collisions via separate chaining).

"""
class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]
        #Creates 1000 buckets (array indices).
        #Each bucket starts with a dummy head node (with key = -1), which simplifies insert/remove logic.
        #Each bucket is initialized with a dummy ListNode(key=-1, val=-1) to simplify insert/delete logic.

    def hash(self, key):
        return key % len(self.map)
    #Maps a key to a bucket index between 0 and 999.


###Go to the correct bucket (self.map[hash(key)])
###Walk the linked list:
###If key is found → update its value.
###If key not found → append a new node at the end.

    def put(self, key: int, value: int):
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

#Traverse the linked list in the correct bucket.
#If key found → return value
#Else → return -1

    def get(self, key: int):
        cur = self.map[self.hash(key)].next   ## ⬅️ Start after dummy
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

#Traverse the linked list and track the previous node (cur).
#If the key is found in cur.next, remove the node by skipping it (cur.next = cur.next.next).

    def remove(self, key: int):
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

