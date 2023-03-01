class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        for i in t:
            if s[0]==t[0]:
                s=s[1:]
            t=t[1:]
            if len(s)==0:
                return True
        return False
