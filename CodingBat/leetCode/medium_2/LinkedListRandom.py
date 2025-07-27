import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        result = self.head.val
        node = self.head.next
        index = 2

        while node:
            # Replace result with current node with 1/index probability
            if random.randint(1, index) == 1:
                result = node.val
            node = node.next
            index += 1

        return result


"""
Approach: Reservoir Sampling
Reservoir sampling is an algorithm to randomly select k items from a stream of unknown size, using only O(1) space.

For this problem (k=1), we:

Traverse the list once

Keep one selected value with a probability of being replaced as we go

Operation	Time	Space
Constructor	O(1)	O(1)
getRandom()	O(n)	O(1)
"""