class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxk=max(piles)
        mink=1
        k=maxk
        while mink<=maxk:
            midk=(mink+maxk)//2
            currh=0
            for i in range(len(piles)):
                currh+=(-(piles[i]//-midk))
            if currh>h:
                mink=midk+1
                continue
            
            k=midk
            maxk=midk-1

        return k