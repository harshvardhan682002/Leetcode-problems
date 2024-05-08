from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res  # Add this line to return the result if the loop completes

# Test cases
strs1 = ["flower","flow","flight"]
solution = Solution()
print(solution.longestCommonPrefix(strs1))  # Output: "fl"

strs2 = ["dog","racecar","car"]
print(solution.longestCommonPrefix(strs2))  # Output: ""
