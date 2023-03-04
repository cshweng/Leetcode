class Solution:
    def longestPalindrome(self, s: str) -> int:
        k = 0
        L = list()
        for i in s:
            if i in L:
                L.remove(i)
                k+=1
            else:
                L.append(i)
        if len(L)==0:
            return 2*k
        else:
            return 2*k+1

