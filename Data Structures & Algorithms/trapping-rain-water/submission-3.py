class Solution:
    def trap(self, height: List[int]) -> int:
        pre=[0]*len(height)
        suff=[0]*len(height)
        max_pre=pre[0]
        max_suff=suff[-1]
        for i in range(1,len(height)):
            pre[i]=max(height[i-1],max_pre)
            max_pre=max(max_pre,height[i-1])

        for i in range(len(height)-2,0,-1):
            suff[i]=max(height[i+1],max_suff)
            max_suff=max(max_suff,height[i+1])

        water=0
        for i in range(1,len(height)-1):
            if height[i]<min(suff[i],pre[i]):
                water+=(min(suff[i],pre[i])-height[i])

        return water