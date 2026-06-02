class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        cf=[0]*26
        for c in s1:
            cf[ord(c)-ord('a')]+=1
        
        l=0

        for r in range(len(s2)):
            c=s2[r]
            cf[ord(c)-ord('a')]-=1

            if max(cf)==0:
                return True

            while cf[ord(c)-ord('a')]<0:
                cf[ord(s2[l])-ord('a')]+=1
                l+=1
        
        return False