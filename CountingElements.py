from typing import List


class Solution:

    def countElements(self, arr: List[int]) -> int:
        ans = 0
        arr.sort()
        for i, num in enumerate(arr):
            for j in range(i + 1, len(arr)):
                if num == arr[j]:
                    continue
                if arr[j] > (num + 1):
                    break
                if num == arr[j] - 1:
                    ans += 1
                    break

        return ans


solution = Solution()
# ans = solution.countElements([1, 2, 3])
# ans = solution.countElements([1, 1, 3, 3, 5, 5, 7, 7])
# ans = solution.countElements([1, 3, 2, 3, 5, 0])
# ans = solution.countElements([1, 1, 2, 2])
ans = solution.countElements([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2])
# ans = solution.countElements([1, 1, 1, 2, 2])
print(ans)
