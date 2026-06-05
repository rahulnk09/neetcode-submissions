class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op=['+','-','*','/']
        for tok in tokens:
            if tok not in op:
                stack.append(int(tok))
            else:
                b=stack.pop()
                a=stack.pop()

                if tok=='+':
                    stack.append(a+b)
                elif tok =='-':
                    stack.append(a-b)
                elif tok == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        
        return int(stack[0])