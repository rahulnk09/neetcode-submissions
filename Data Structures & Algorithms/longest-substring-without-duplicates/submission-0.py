class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        sub=[s[0]]
        res=1
        answer=0
        for i in range(1,len(s)):
            if s[i]==sub[0]:
                print(sub.pop(0))
                sub.append(s[i])

            elif s[i] in sub:
                answer=max(answer,res)
                indx=sub.index(s[i])
                sub=sub[indx+1:]
                sub.append(s[i])
                res=len(sub)

            else:
                sub.append(s[i])
                res+=1
        
        return max(answer,res)