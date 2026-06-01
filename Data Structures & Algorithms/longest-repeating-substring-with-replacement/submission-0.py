class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if not s:
            return 0

        cf=[0]*26

        l,r=0,0
        res=0
        
        while r<len(s):
            
            cf[ord(s[r])-ord('A')]+=1
            if (r-l+1)-max(cf)>k:
                cf[ord(s[l])-ord('A')]-=1
                l+=1
            

            res=max(res,(r-l+1))
            r+=1

        return res


        