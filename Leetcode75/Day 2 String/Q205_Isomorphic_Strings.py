class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
                return False
        def swap(s,t):
            hashtable = dict(zip(s,t))
            for i in range(len(s)):
                if hashtable[s[i]]!=t[i]:
                    return False
            return True
        return swap(s,t) and swap (t,s)
