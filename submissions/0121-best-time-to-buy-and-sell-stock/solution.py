class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 Pointer solution.
        # We loop through list incrementing left to right if buy > sell
        # We always increment sell price
        # We use a running profit calc and return it at the end
        l,r = 0,1
        profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l=r
                r+=1
            else:
                profit = max(profit, prices[r] - prices[l])
                r+=1
        return profit
