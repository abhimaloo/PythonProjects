class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()
        for n in nums:
            if n in duplicates:
                return True
            else:
                duplicates.add(n)
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()
        for n in nums:
            if n in duplicates:
                print(f"Duplicate found: {n}")
            else:
                duplicates.add(n)
        return False

class Solution:
    def duplicate_string(s) -> bool:
        duplicates = set()
        for char in s:
           if char in duplicates:
               print(f"Duplicate found: {char}")
           else:
               duplicates.add(char)

# hashMap
class Solution:
    def dup_using_hashmap(nums):
       count_map = {}

       for num in nums:
           if num in count_map:
               count_map[num] +=1
           else:
               count_map[num] = 1

       for num , count in count_map.items():
           if count > 1:
               print(f"{num}: {count}")

#duplicate words in string
    def dup_words_string(s):
        words = s.split()
        word_count = {}
        duplicates = []

        for word in words:
            if word in word_count:
                word_count[word] +=1
            else:
                word_count[word] = 1

        for word , count in word_count.items():
            if count > 1:
                duplicates.append(word)

        return duplicates




