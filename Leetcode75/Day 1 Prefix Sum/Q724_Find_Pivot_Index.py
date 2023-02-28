class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums[1:])
        for i in range(0,len(nums)):
            if left==right: 
                return i
            left += nums[i]
            try:
                right -= nums[i+1]
            except:
                pass
        else:
            return -1