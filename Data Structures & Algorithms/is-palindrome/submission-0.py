class Solution:
    def isPalindrome(self, s: str) -> bool:
        p=0
        q=len(s)-1
        while p<q:
            if not s[p].isalnum():
                p+=1
                continue
            if not s[q].isalnum():
                q-=1
                continue
            if s[p].isalnum() and s[q].isalnum():
                if s[p].lower()==s[q].lower():
                    p+=1
                    q-=1
                else:
                    return False
        return True