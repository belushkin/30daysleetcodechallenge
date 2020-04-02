class Solution:

    def isHappy(self, n: int) -> bool:
        return self.checkHappyNumber(n, 0)

    def checkHappyNumber(self, n: int, count: int) -> bool:
        res = 0
        while n > 0:
            res += (n % 10)**2
            n = n // 10

        return True if res == 1 else False if count > 100 else self.checkHappyNumber(res, count + 1)

solution = Solution()
print(solution.isHappy(7))
