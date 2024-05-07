from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return res
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

sol = Solution()

strs = ["flower","flow","flight"]
print(sol.longestCommonPrefix(strs))

strs = ["dog","racecar","car"]
print(sol.longestCommonPrefix(strs))
