class Solution:
    def reverseWords(self, s: List[str]) -> None:
        #Step 1 = helper function This reverses the characters between indices l and r inclusive.
        def reverse(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]   # Swap characters
                l += 1
                r -= 1

        # Step 2: Reverse the entire list
        reverse(0, len(s) - 1)  #This puts the words in reverse order, but the individual words are also reversed.

        # Step 3: Reverse each word individually to fix them
        start = 0
        for end in range(len(s) + 1):
            if end == len(s) or s[end] == ' ':
                reverse(start, end - 1)
                start = end + 1


"""
This loop does:
Go through each character in the list.
When a space ' ' or end of list is found:
It means the current word is from start to end - 1.
It reverses the characters of that word.
Then moves start to the beginning of the next word.

Summary
Step	Description
Step 1	Reverse the whole list to reverse word order
Step 2	Reverse each word to fix its letter order
Space	O(1) (in-place)
Time	O(n) — each character is touched twice





"""