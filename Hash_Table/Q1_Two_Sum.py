class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            try:
                return([hashTable[target - nums[i]],i])
            except:
                hashTable[nums[i]]=i
        return []

