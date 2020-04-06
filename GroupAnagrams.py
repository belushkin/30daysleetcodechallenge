from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for str in strs:
            res.setdefault(''.join(sorted(str)), []).append(str)

        return list(res.values())


solution = Solution()
# ans = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
ans = solution.groupAnagrams(["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"])

print(ans)
