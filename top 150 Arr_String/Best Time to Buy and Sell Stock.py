from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")   # start with very high value
        max_profit = 0             # best profit so far
        
        for price in prices:
            min_price = min(min_price, price)  # update min price so far
            max_profit = max(max_profit, price - min_price)  # update profit if better
        return max_profit

        
print(Solution().maxProfit([7,1,5,3,6,4]))  # Output: 5
print(Solution().maxProfit([7,6,4,3,1]))    # Output: 0
