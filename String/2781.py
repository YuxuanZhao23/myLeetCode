# You are given a string word and an array of strings forbidden.

# A string is called valid if none of its substrings are present in forbidden.

# Return the length of the longest valid substring of the string word.

# A substring is a contiguous sequence of characters in a string, possibly empty.

from ast import List


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        # timeout
        # return self.slidingWindow(word, forbidden)

        return self.encode(word, forbidden)

    def encode(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden) # use hash to improve string comparison
        res = 0
        right = len(word)
        for left in range(len(word)-1, -1, -1):
            # notice that 1 < len(forbidden[i]) <= 10
            for k in range(left, min(right, left + 10)):
                if word[left: k+1] in forbidden:
                    right = k
                    break
            res = max(res, right - left)
        return res
        

    def slidingWindow(self, word: str, forbidden: List[str]) -> int:
        # len(word) = n, len(forbidden) = m, Time Complexity: O(nm)
        left = 0
        res = 0
        for right in range(1, len(word)+1):
            flag = True
            while flag:
                flag = False
                for f in forbidden:
                    if len(f) <= right - left:
                        if f == word[left: left + len(f)]:
                            left += 1
                            flag = True
                            break
                        elif f == word[right - len(f): right]:
                            left = right - len(f) + 1
                            flag = True
                            break
                        
            res = max(right - left, res)
        return res