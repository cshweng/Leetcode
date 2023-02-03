class Solution:
#  recurcive O(2^n)
#     def climbStairs(self, n: int) -> int:  
#         def step(n,memo = {}):
#             if n == 1:
#                 return 1
#             elif n == 2:
#                 return 2
#             return step(n-2)+step(n-1)
#         return step(n)

# recurcive + memo O(n)
    def climbStairs(self, n: int) -> int:  
        def step(n,memo = {}):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            try:
                return memo[n]
            except:
                result = step(n-2,memo)+step(n-1,memo)
                memo[n] = result
                return result
        return step(n)
