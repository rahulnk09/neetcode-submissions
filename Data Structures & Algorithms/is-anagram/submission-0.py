class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        for i in range(len(s)):
            let=s[i]
            if s[i] in s_dict:
                
                s_dict[let]=s_dict[let]+1
            else:
                s_dict[let] = 1
        
        t_dict={}
        for i in range(len(t)):
            let=t[i]
            if t[i] in t_dict:
                
                t_dict[let]=t_dict[let]+1
            else:
                t_dict[let]=1

        if s_dict == t_dict:
            return True
        else:
            return False
        