from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        value = at = start = 0

        if len(prices) <= 1:
            return 0

        for cur, e in enumerate(prices):
            at = cur + 1 if at < len(prices)-1 else start
            if prices[cur] > prices[at]:
                value += prices[cur] - prices[start]
                start = at

        return value


solution = Solution()
# profit = solution.maxProfit([7, 1, 5, 3, 6, 4])
profit = solution.maxProfit([1, 2, 3, 4, 5])
# profit = solution.maxProfit([7, 6, 4, 3, 1])
# profit = solution.maxProfit([0, 3, 2, 4])
# profit = solution.maxProfit([0, 3])

print(profit)
