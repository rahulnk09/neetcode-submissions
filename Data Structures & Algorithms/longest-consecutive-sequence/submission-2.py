class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        start=[]
        for i in range(len(nums)):
            if nums[i]-1 not in s:
                start.append(nums[i])
        res=0
        for n in start:
            t=1
            while n+1 in s:
                t+=1
                n=n+1
            res=max(res,t)
        return res