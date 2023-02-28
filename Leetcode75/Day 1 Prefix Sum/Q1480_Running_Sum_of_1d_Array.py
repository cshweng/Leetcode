class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = 0
        L =[]
        for i in nums:
            result += i
            L.append(result)
        return L
