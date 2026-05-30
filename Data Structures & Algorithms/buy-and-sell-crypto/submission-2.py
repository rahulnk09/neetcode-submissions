class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        pr=0
        buy=prices[0]
        
        for i in range(1,len(prices)):
            pr=max(pr,prices[i]-buy)
            buy=min(buy,prices[i])

        return pr
        