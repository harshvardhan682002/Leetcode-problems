class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"} #dictionary maps each closing bracket to its corresponding opening bracket
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
sol = Solution
s = "()"
solution = Solution()
result = solution.isValid(s)
print(result) # Output: True (balanced parentheses)
s = "()[]{}"
solution = Solution()
result = solution.isValid(s)
print(result) # Output: True (balanced parentheses)
s = "(]"
solution = Solution()
result = solution.isValid(s)
print(result) # Output: False (not balanced parentheses)