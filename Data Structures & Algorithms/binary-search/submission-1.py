class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Excellent edge-case checks
        if not nums or nums[0] > target or nums[-1] < target:
            return -1
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            midv = nums[mid]

            if midv == target:
                return mid
            elif midv > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1