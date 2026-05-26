class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:  # Quick edge case check for empty input
            return 0
            
        nums.sort()
        res = 0
        i = 0 
        
        while i < len(nums):
            t = 1
            hit_else = False
            
            for j in range(i+1, len(nums)):
                if nums[j] == nums[i] + t:
                    t += 1
                elif nums[j] == nums[i] + t - 1:
                    continue  # Handles duplicate values beautifully!
                else:
                    i = j     # Jump your outer loop pointer to the new sequence
                    hit_else = True
                    break
            
            res = max(res, t)
            
            # FIX: If the inner loop finished naturally without breaking, 
            # it means we processed everything up to the last element.
            if not hit_else:
                break 
                
        return res