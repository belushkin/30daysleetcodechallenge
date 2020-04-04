from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i, e in reversed(list(enumerate(nums))):
            if e == 0:
                nums.append(nums.pop(i))


solution = Solution()
# nums = [0,1,0,3,12]
nums = [0, 0, 1]
solution.moveZeroes(nums)
print(nums)
