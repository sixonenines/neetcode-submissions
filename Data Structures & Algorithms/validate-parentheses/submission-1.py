class Solution:
    def isValid(self, s: str) -> bool:
        stacks=[]
        dictMap={"(":")","[":"]","{":"}"}
        for char in s:
            if char=="(" or char=="{" or char=="[":
                stacks.append(char)
            if char==")" or char=="}" or char=="]":
                if len(stacks)==0:
                    return False
                if dictMap[stacks[len(stacks) - 1]] == char:
                    stacks.pop()
                else:
                    return False
        if len(stacks)==0:
            return True
        else:
            return False