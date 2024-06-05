#Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
# Define a class named AddDigits
class AddDigits:
    # Define a method within the class that takes an integer 'num' as input
    def addDigits(self, num: int) -> int:
        # Check if the input number is zero
        if num == 0:
            # If the number is zero, return zero
            return 0
        else:
            # For any other number, compute the digital root using the formula
            return 1 + (num - 1) % 9

# Create an instance of the AddDigits class
Add_Digits = AddDigits()
# Define a variable
num = 38
print(Add_Digits.addDigits(num)) #output 2
num = 0
print(Add_Digits.addDigits(num)) #output 0