from typing import List
import math


## You can buy stocks as many times as possible
class Solution:
    ## Check if there is upward
    # change then add it in profit
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0;
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

Sol = Solution()
print(Sol.maxProfit([7, 1, 5, 3, 6, 4]))
