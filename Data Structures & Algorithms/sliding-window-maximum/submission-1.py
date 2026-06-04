class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l=0
        r=k-1
        maxs=[]
        cm=-10000000
        cmp=0

        for i in range(k):
            if cm<nums[i]:
                cmp=i
                cm=nums[i]
        maxs.append(cm)
        
        while r<len(nums)-1:
            l+=1
            r+=1
            if cm<=nums[r]:
                cm=nums[r]
                cmp=r
                maxs.append(cm)
                continue
            if cmp<l:
                
                cm=nums[l]
                cmp=l
                j=l+1
                while j<=r:
                    if cm<=nums[j]:
                        cmp=j
                        cm=nums[j]
                    j+=1
                maxs.append(cm)
            # elif nums[r]>=cm:
            #     cm=nums[r]
            #     cmp=r
            #     maxs.append(cm)
            else:
                maxs.append(cm)
        return maxs