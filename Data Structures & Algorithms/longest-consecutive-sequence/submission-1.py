class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        nums.sort()
        for i in range(len(nums)):
            seq=[nums[i]]
            for j in range(i+1,len(nums)):

                if nums[j]==(seq[-1]+1):
                    seq.append(nums[j])

            res=max(res,len(seq))
        
        return res