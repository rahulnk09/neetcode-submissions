class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        charset=set()
        l=0
        r=1
        charset.add(s[l])
        
        ans=1
        while r<len(s):
            if s[r] in charset:
                
                while s[r] in charset and l<r:
                    charset.remove(s[l])
                    l+=1

            charset.add(s[r])
            ans=max(ans,(r-l+1))
            r+=1

        return ans