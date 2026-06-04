from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # Stores INDICES, not the actual numbers
        res = []
        
        for i in range(len(nums)):
            # STEP 1: Remove indices that are no longer in the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
                
            # STEP 2: Remove smaller numbers from the right
            # If the current number is bigger than the ones at the back of the queue,
            # those older, smaller numbers can NEVER be the maximum anymore. Kick them out!
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
                
            # STEP 3: Add the current index to the queue
            dq.append(i)
            
            # STEP 4: Once our window has reached size 'k', record the maximum.
            # Because of Step 2, the largest number is ALWAYS at the very front of the queue.
            if i >= k - 1:
                res.append(nums[dq[0]])
                
        return res