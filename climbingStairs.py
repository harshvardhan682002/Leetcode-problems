#You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
class climbingStairs:
    # This method calculates the number of ways to climb 'n' stairs.
    def climbStair(self, n: int) -> int:
        one, two = 1, 1  # Initialize the first two base cases (n=1 and n=2)
        # Loop from 0 to n-2 (since we already know the ways to climb 1 and 2 stairs)
        for i in range(n - 1):
            temp = one  # Store the current number of ways to climb i stairs
            one = one + two  # Update the number of ways to climb i+1 stairs
            two = temp  # Update the number of ways to climb i-1 stairs
        return one  # Return the number of ways to climb n stairs

climbing_Stairs = climbingStairs()  # Create an instance of the climbingStairs class

n = 2
result = climbing_Stairs.climbStair(n)  # Calculate the number of ways to climb 2 stairs
print(f"The number of ways to climb {n} stairs is: {result}")

n = 3
result = climbing_Stairs.climbStair(n)  # Calculate the number of ways to climb 3 stairs
print(f"The number of ways to climb {n} stairs is: {result}")
