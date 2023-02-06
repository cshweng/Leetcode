class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        dic = {}
        L = []
        for i in range(n):
            dic[nums[i]] = nums[i+n]
            L.append(nums[i])
            L.append(dic[nums[i]])
        return L

