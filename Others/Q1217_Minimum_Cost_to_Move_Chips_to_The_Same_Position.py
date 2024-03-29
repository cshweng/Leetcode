class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_cnt = 0
        even_cnt = 0
        for i in position:
            if i % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
        return min(even_cnt, odd_cnt)