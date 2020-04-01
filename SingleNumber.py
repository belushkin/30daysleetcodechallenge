from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        freq = {v: k for k, v in freq.items()}
        return freq[1]


solution = Solution()

print(solution.singleNumber([2, 2, 1, 1, 3]))
