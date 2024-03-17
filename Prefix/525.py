class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = {0: -1}
        count = res = 0
        for i, num in enumerate(nums):
            if num == 1: 
                count += 1
            else: 
                count -= 1
            if count not in prefix:
                prefix[count] = i
            else:
                res = max(res, i - prefix[count])

        return res