# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward
class Solution(object):
    def isPalindrome(self, x):
        # Check if x is negative, negative numbers can't be palindromes
        if x < 0:
            return False
        # Check if x is 0, 0 is considered a palindrome
        if x == 0:
            return True
        # If the last digit of x is 0 and x is not 0 itself, it can't be a palindrome
        if x % 10 == 0:
            return False
        
        originalX = x
        numReversed = 0
        while x > 0:
            lastDigit = x % 10 
            numReversed = numReversed * 10 + lastDigit
            x = x // 10 
            
        return numReversed == originalX
sol = Solution()
print(sol.isPalindrome(121)) # true
print(sol.isPalindrome(-121)) # false
print(sol.isPalindrome(10)) # false