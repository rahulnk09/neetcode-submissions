class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxr=0
        for i,h in enumerate(heights):
            start=i

            while stack and stack[-1][1]>h:
                pi,ph=stack.pop()

                maxr=max(maxr,ph*(i-pi))

                start=pi
            
            stack.append((start,h))
        
        for i,h in stack:
            maxr=max(maxr,h*(len(heights)-i))

        return maxr