class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter={}
        for num in nums:
            counter[num]=1+counter.get(num,0)

        arr=[[] for i in range(len(nums)+1)]

        for num,count in counter.items():
            arr[count].append(num)
        
        res=[]
        for i in range(len(nums),0,-1):
            for n in arr[i]:
                res.append(n)
                if len(res)==k:
                    return res
                    