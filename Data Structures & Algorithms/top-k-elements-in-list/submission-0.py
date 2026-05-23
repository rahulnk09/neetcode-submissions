class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter={}
        for num in nums:
            counter[num]=1+counter.get(num,0)
        
        counter=sorted(counter,key=counter.get, reverse=True)

        return counter[:k]