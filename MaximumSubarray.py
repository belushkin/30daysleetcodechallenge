from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = 0
        res = -9999999999
        for num in nums:
            m = num + m if res > 0 else num + 0
            res = max(res, m, num)
            if res > 0 >= m:
                m = num if num > 0 else 0
        return res


solution = Solution()
print(solution.maxSubArray([-2, 3, 1]))
