# Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

# Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

# Similar Question: 31

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = [int(c) for c in str(n)]
        if nums == None or len(nums) == 0: return
        rs = len(nums)-2
        while rs >= 0 and nums[rs] >= nums[rs+1]: rs -= 1
        if rs >= 0:
            rl = len(nums)-1
            while nums[rl] <= nums[rs]: rl -= 1
            nums[rs], nums[rl] = nums[rl], nums[rs]
        left = rs+1
        right = len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left+1, right-1
        res = int(''.join([str(n) for n in nums]))
        return res if res > n and res < 2 ** 31 else -1