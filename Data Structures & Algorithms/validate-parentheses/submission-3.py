from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        op=['(','{','[']
        mp={'}':'{',
            ']':'[',
            ')':'('}
        dq=deque()

        for c in s:
            if c in op:
                dq.append(c)
            elif dq:
                cpo=mp[c]
                if dq[-1]==cpo:
                    dq.pop()
                else:
                    return False
            else:
                return False
            
        if dq:
            return False
        else:
            return True
        