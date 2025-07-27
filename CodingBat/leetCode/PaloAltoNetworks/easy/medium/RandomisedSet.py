import random

class RandomizedSet:

    def __init__(self):
        self.arr = []              # stores the values
        self.val_to_index = {}     # maps val → index in arr

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False #If val already exists → don't insert → return False
        self.arr.append(val)  # append value to the list
        self.val_to_index[val] = len(self.arr) - 1  # Store its index in the map
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False  # If the value doesn’t exist, return False

        # Swap with the last element for O(1) removal   #Swap-Delete Trick (to delete in O(1)):
        idx = self.val_to_index[val]  #index of value to remove
        last_val = self.arr[-1]       #  # get the last element


        self.arr[idx] = last_val   # Move last_val into val's position
        self.val_to_index[last_val] = idx #Update map to reflect last_val’s new index

        # Remove last element
        self.arr.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)

"""
Support 3 operations efficiently:
insert(val) → Add val if it doesn’t exist.
remove(val) → Remove val if it exists.
getRandom() → Return a random element with equal probability.
Use two structures:
1. self.arr:
Stores the actual values in a list → allows:
Fast random access (for getRandom)
Easy element swapping for remove
2. self.val_to_index:
A hash map to track each value's index in the list → allows:
Fast lookup for insert and remove




"""