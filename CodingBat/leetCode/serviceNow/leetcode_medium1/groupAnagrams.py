'''
time = complexity
O(n * k log k)
n: number of strings

k: average length of each string

k log k: cost to sort each string
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagram_map = defaultdict(list)

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)

        for value in anagram_map.values():
            result.append(value)

        return result


solution # 2

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            sorted_s = tuple(sorted(s))
            if sorted_s not in anagram_map:
                anagram_map[sorted_s] = []
            anagram_map[sorted_s].append(s)

        return list(anagram_map.values())


"""
A defaultdict from the collections module is used here.
It automatically initializes an empty list when a new key is accessed.
This dictionary (anagram_map) will map sorted strings (used as keys) to a list of original strings that are anagrams of each other.
For every string s in the input list:
sorted(s) sorts the characters in the string. For example, 'eat' becomes ['a', 'e', 't'].
tuple(sorted(s)) converts the list to a tuple, which is hashable and can be used as a dictionary key.
This sorted_s becomes a unique identifier for all anagrams with those letters.
We append the original string s to the list associated with that sorted tuple in anagram_map.

Time complexity:
Sorting each word takes O(k log k), where k = length of the word.
Total time: O(n * k log k), where n = number of words.
Space complexity: O(nk) for storing the groups.
"""








