#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.
class ValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

# Creating an instance of the ValidPalindrome class
valid_palindrome = ValidPalindrome()

# Testing the isPalindrome method
s1 = "A man, a plan, a canal: Panama"
print(valid_palindrome.isPalindrome(s1))  # Output: True

s2 = "race a car"
print(valid_palindrome.isPalindrome(s2))  # Output: False
