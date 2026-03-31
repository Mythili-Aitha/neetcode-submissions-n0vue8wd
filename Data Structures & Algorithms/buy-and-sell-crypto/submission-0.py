class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        mi = prices[0]
        for s in prices:
            m = max(m, s-mi)
            mi = min(mi, s)
        return m
            


        