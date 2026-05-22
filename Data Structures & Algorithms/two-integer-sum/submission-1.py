class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps={nums[0]:0}
        for i in range(1,len(nums)):
            diff=target-nums[i]
            if diff in maps:
                return [maps[diff],i]
            maps[nums[i]]=i
        

        