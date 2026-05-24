class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]*len(nums)
        suff=[1]*len(nums)
        j=len(nums)-2
        for i in range(1,len(nums)):
            pre[i]=pre[i-1]*nums[i-1]
            suff[j]=suff[j+1]*nums[j+1]

            j-=1
        
        return [x*y for x,y in zip(pre,suff)]