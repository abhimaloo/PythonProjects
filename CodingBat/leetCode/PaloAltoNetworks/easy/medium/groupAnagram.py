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
            sorted_s = tuple(sorted(s))  #Because tuples are hashable,
            # but lists are not — and dictionary keys (like anagram_map[sorted_s]) must be hashable.
            #Tuples are immutable and hashable
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











