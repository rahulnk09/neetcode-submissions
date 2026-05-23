class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr=[[0]*26 for i in range(len(strs))]
        i=0
        for st in strs:
            for char in st:
                arr[i][ord(char)-ord('a')]+=1
            i+=1
        
        result=[]
        seen={}
        for i, row in enumerate(arr):
            row=tuple(row)
            if row not in seen:
                seen[row]=[]
            seen[row].append(strs[i])
        return(list(seen.values()))