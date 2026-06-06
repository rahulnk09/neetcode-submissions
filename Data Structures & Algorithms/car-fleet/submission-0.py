import numpy as np
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[(target-pos)/sp for pos,sp in zip(position,speed)]
        
        pos=np.array(position)
        t=np.array(time)

        si=np.argsort(pos)[::-1]

        pos=pos[si]
        t=t[si]

        stack=[t[0]]
        for i in range(1,len(pos)):
            #print(i)
            if stack[-1]>=t[i]:
                continue
            stack.append(t[i])
        return len(stack)
                





