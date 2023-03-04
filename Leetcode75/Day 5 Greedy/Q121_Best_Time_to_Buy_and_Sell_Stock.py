class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_=0
        min_=0
        L=0
        for i in range(1,len(prices)):
            if prices[i]< prices[min_]:
                min_ = i
                max_ = i
            if prices[i]>prices[max_]:
                max_ = i
            if prices[max_]-prices[min_]>L:
                L = prices[max_]-prices[min_]
        return L

