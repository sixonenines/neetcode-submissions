class Solution:
    def isValid(self, s: str) -> bool:
        stacks=[]
        dictMap={")":"(","]":"[","}":"{"}
        # Tip: Reverse key value pair if they are unique. Do this depending on what you want to
        # get
        for char in s:
            if char in dictMap:
                if stacks and stacks[-1]==dictMap[char]:
                    stacks.pop()
                else:
                    return False

            else:
                stacks.append(char)
        return not bool(stacks)
        return True if not stack else False