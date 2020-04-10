import re


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        while re.search('#', S) and re.search('\w', S):
            S = re.sub('\w#', '', S)
            S = re.sub('^#(\w)', r'\1', S)
            S = re.sub('^##', '#', S)
        S = re.sub('#', '', S)

        while re.search('#', T) and re.search('\w', T):
            T = re.sub('\w#', '', T)
            T = re.sub('^#(\w)', r'\1', T)
            T = re.sub('^##', '#', T)
        T = re.sub('#', '', T)

        # print("S: " + S + ", T: " + T)
        return S == T


solution = Solution()
solution.backspaceCompare('ab#c', 'ad#c')
solution.backspaceCompare('ab##', 'c#d#')
solution.backspaceCompare('a##c', '#a#c')
solution.backspaceCompare('a#c', 'b')
solution.backspaceCompare('#abc#', '####cb##aa#ssss################################################f')
solution.backspaceCompare('ab###c#####g###', 'ad#c')
