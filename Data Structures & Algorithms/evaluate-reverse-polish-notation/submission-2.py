class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            res=token
            if token=="/":
                # a,b = stack.pop(),stack.pop()
                optwo=stack.pop()
                opone=stack.pop()
                res=opone/optwo
            if token=="+":
                optwo=stack.pop()
                opone=stack.pop()
                res=opone+optwo
            if token=="-":
                optwo=stack.pop()
                opone=stack.pop()
                res=opone-optwo
            if token=="*":
                optwo=stack.pop()
                opone=stack.pop()
                res=opone*optwo
            stack.append(int(res))
        return stack[0]