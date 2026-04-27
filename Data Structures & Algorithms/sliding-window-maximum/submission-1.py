from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        result = []
        
        for i in range(len(nums)):
            # 1. Remove indices that are out of the current window range
            if dq and dq[0] < i - k + 1:
                dq.popleft()
                
            # 2. Maintain monotonic decreasing order
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
                
            # 3. Add current index
            dq.append(i)
            
            # 4. Record the max element once the first window is full
            if i >= k - 1:
                result.append(nums[dq[0]])
                
        return result

# This part matches what your main.py is trying to do:
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 1, 0, 4, 2, 6]
    k = 3
    print(solution.maxSlidingWindow(nums, k))