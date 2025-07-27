class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount, sCount = {}, {}
        #If p is longer than s, it’s impossible to find any anagrams
        if len(p) > len(s):
            return []
        #Build character counts for both p and the first window of s
        for i in range(len(p)):
            pCount[p[i]] = pCount.get(p[i], 0) + 1
            sCount[s[i]] = sCount.get(s[i], 0) + 1

        #If the first window matches, index 0 is a valid anagram
        if pCount == sCount:
            result = [0]
        else:
            result = []

        #Step 2: Sliding Window
        l = 0
        #Start moving the right edge r of the window one character at a time, keeping the window size fixed at len(p)
        for r in range(len(p), len(s)):
            sCount[s[r]] = sCount.get(s[r], 0) + 1  #Add the new right character to sCount
            sCount[s[l]] -= 1   #Remove the leftmost character from the count

            if sCount[s[l]] == 0:   #Clean up zero counts to keep the map comparable with pCount
                sCount.pop(s[l])

            l += 1   #Slide the left pointer

            if pCount == sCount:   #If counts match, this window is an anagram; add its starting index
                result.append(l)

        return result


"""
We use a sliding window of length len(p) to track character counts in s 
and compare them to p's character counts.
pCount: character frequency of p
sCount: character frequency of the current window in s
Time and Space Complexity
Time Complexity: O(n)

Building and updating hash maps takes constant time per step (since the alphabet is small)

Space Complexity: O(1)

Max 26 characters in the hash maps





"""










