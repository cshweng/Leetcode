class Solution:
    def tribonacci(self, n: int) -> int:
        L = [0,1,1]
        if n <3:
            return L[n]
        else:
            for i in range(n-3):
                L.append(sum(L))
                L.pop(0)
            return sum(L)
# ----deque-----
class Solution:
    def tribonacci(self, n: int) -> int:
        from collections import deque
        L = deque([0,1,1])
        if n <3:
            return L[n]
        else:
            for i in range(n-3):
                L.append(sum(L))
                L.popleft()
            return sum(L)