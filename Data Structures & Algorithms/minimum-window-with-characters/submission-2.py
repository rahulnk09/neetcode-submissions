class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s) or t=="":
            
            return ""

        cf={}

        for c in t:
            cf[c]=cf.get(c,0)+1
        
        need=len(cf)
        have=0
        wf=dict.fromkeys(cf,0)

        res=""
        rl=10000000000

        l=0

        for r in range(len(s)):

            c=s[r]

            if c in cf:
                
                wf[c]+=1
                if wf[c]==cf[c]:
                    have+=1
            
            while have==need:
                if rl>(r-l+1):
                    rl=(r-l+1)
                    res=s[l:r+1]
                if s[l] in wf:
                    wf[s[l]]-=1
                    if wf[s[l]]<cf[s[l]]:
                        have-=1
                l+=1

        return res

            
