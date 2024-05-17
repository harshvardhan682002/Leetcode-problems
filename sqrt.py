class Sqrt:
    def mySqrt(self, x: int) -> int:
        # Initialize left and right pointers for binary search
        l, r = 0, x
        # Initialize a variable to store the result
        res = 0

        # Binary search loop
        while l <= r:
            # Calculate the midpoint
            m = l + ((r - l) // 2)  # Fix: Changed (r - 1) to (r - l) to calculate mid correctly
            
            # If the square of the midpoint is greater than x, move the right pointer to mid - 1
            if m ** 2 > x:
                r = m - 1
            # If the square of the midpoint is less than x, move the left pointer to mid + 1
            elif m ** 2 < x:
                l = m + 1
                # Update the result to the current midpoint
                res = m
            # If the square of the midpoint is equal to x, return the midpoint
            else:
                return m
        
        # Return the result
        return res

# Create an instance of the Sqrt class
sqrt_num = Sqrt()

# Test case 1: x = 4
x = 4
# Print the square root of 4
print(sqrt_num.mySqrt(x))

# Test case 2: x = 8
x = 8
# Print the square root of 8
print(sqrt_num.mySqrt(x))
