from typing import List
import math


## You can buy stocks as many times as possible
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minList = [0] * len(prices)
        maxList = [0] * len(prices)

        minList[0] = prices[0]
        maxList[len(prices) - 1] = prices[len(prices) - 1]

        for i in range(1, len(prices)):
            minList[i] = min(prices[i], minList[i - 1])

        for i in range(len(prices) - 2, 0, -1):
            maxList[i] = max(prices[i], maxList[i + 1])

        profit = [x - y for x, y in zip(maxList, minList)]

        return max(profit)


Sol = Solution()
print(Sol.maxProfit([7,6,4,3,1]))
