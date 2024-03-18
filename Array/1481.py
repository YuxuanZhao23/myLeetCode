# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        for i, n in enumerate(sorted(count.values())):
            if n <= k:
                k -= n
            else:
                return len(count.keys()) - i
        return 0