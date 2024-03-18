# 1481. Least Number of Unique Integers after K Removals

# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.



class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # return self.sortApproach(arr, k)
        return self.countingSortApproach(arr, k)

    # Space Complexity: O(N)
    # Time Complexity: O(N)
    def countingSortApproach(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        # counting sort for "times", since we don't care specific number
        frequencies = [0] * (len(arr) + 1)
        for c in count.values():
            frequencies[c] += 1
        res = len(count)
        for times in range(1, len(arr)+1):
            num_remove = min(k // times, frequencies[times])
            k -= times * num_remove
            res -= num_remove
            if k < times+1: return res
        return 0

    # Space Complexity: O(M)
    # Time Complexity: O(N + MlogM)
    def sortApproach(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        for i, n in enumerate(sorted(count.values())):
            if n <= k:
                k -= n
            else:
                return len(count.keys()) - i
        return 0