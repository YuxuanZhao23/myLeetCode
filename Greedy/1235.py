# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

# You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

# If you choose a job that ends at time X you will be able to start another job that starts at time X.

# 不相交区间 => 按 end time 排序

def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = [(endTime[i], i) for i in range(len(endTime))]
        intervals.sort() # O(nlogn)
        dp = {0:0}
        indices = deque([0])
        for end, i in intervals: # O(nlogn)
            # binary search for the closest last exist
            left = 0
            right = len(indices)-1
            while left < right:
                mid = left + (right - left)//2
                if indices[mid] <= startTime[i]:
                    right = mid
                else:
                    left = mid + 1
            dp[end] = max(dp[indices[left]] + profit[i], dp[indices[0]])
            indices.appendleft(end)
        return dp[intervals[-1][0]]