class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Quick optimization check
        if max(nums) < 0 or min(nums) > 0:
            return []

        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # FIX 1: Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Embedded two-pointer approach (replaces separate two_sum)
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            
            while l < r:
                current_sum = nums[l] + nums[r]
                
                if current_sum > target:
                    r -= 1
                elif current_sum < target:
                    l += 1
                else:
                    # Found a valid triplet!
                    result.append([nums[i], nums[l], nums[r]])
                    
                    # FIX 2: Skip duplicate values for the second number
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # FIX 2: Skip duplicate values for the third number
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                        
                    # Move both pointers inward to look for MORE pairs for the same nums[i]
                    l += 1
                    r -= 1
                    
        return result