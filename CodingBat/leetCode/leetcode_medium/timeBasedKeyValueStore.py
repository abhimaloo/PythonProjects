from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)  # key: [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.store.get(key, [])

        # run binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return result

    # Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

"""
You need to implement a class TimeMap that supports:

set(key, value, timestamp): Stores the key with the given value and timestamp.

get(key, timestamp): Returns the value with the largest timestamp less than or equal to the given timestamp.

✅ 1. set(key, value, timestamp)
python
Copy
Edit
self.store[key].append([value, timestamp])
✅ Time Complexity: O(1)
Appending to a list is constant time.

✅ Space Complexity: O(1) per call
You store one [value, timestamp] pair per call.

Across n calls, the total space is O(n).

 2. get(key, timestamp)
 
 Time Complexity: O(log k)
Where k = number of timestamps stored for the given key.

You binary search in a list of size k.

✅ Space Complexity: O(1)
You use a few pointers and variables — constant space.







"""