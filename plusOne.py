#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

#Increment the large integer by one and return the resulting array of digits. 
from typing import List

class PlusOne:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Reverse the digits list to make it easier to work with
        digits = digits[::-1]
        
        # Initialize variables one (to represent carrying one) and i (to keep track of the current digit index)
        one, i = 1, 0
        
        # Iterate through the digits list until there's no carrying one left
        while one:
            # If we're within the bounds of the digits list
            if i < len(digits):
                # If the current digit is 9, set it to 0 and continue carrying one to the next digit
                if digits[i] == 9:
                    digits[i] = 0
                # If the current digit is not 9, add one to it and set one to 0 to stop the loop
                else:
                    digits[i] += 1
                    one = 0
            # If we've reached the end of the digits list, append 1 to the list to represent carrying one
            else:
                digits.append(1)
                one = 0
            # Move to the next digit index
            i += 1
        
        # Reverse the digits list back to its original order and return
        return digits[::-1]

# Create an instance of the PlusOne class
plus = PlusOne()

# Test case
digits = [1, 2, 3]
result = plus.plusOne(digits)
print(result)

# Test case
digits = [4,3,2,1]
result = plus.plusOne(digits)
print(result)
# Test case
digits = [9]
result = plus.plusOne(digits)
print(result)