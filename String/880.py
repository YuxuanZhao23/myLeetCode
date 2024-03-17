
# You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

# If the character read is a letter, that letter is written onto the tape.
# If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
# Given an integer k, return the kth letter (1-indexed) in the decoded string.
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        l = 0
        for i, c in enumerate(s):
            if c.isdigit(): l *= int(c)
            else: l += 1
            if l >= k: break
        for j in range(i, -1, -1):
            if s[j].isdigit():
                l /= int(s[j])
                k %= l
            else:
                if k == 0 or k == l: return s[j]
                l -= 1