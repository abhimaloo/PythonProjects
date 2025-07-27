import random

class RandomizedSet:

    def __init__(self):
        self.arr = []              # stores the values
        self.val_to_index = {}     # maps val → index in arr

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.arr.append(val)
        self.val_to_index[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        # Swap with the last element for O(1) removal
        idx = self.val_to_index[val]
        last_val = self.arr[-1]

        self.arr[idx] = last_val
        self.val_to_index[last_val] = idx

        # Remove last element
        self.arr.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
