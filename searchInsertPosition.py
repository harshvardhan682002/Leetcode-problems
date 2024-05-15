# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
from typing import List

# Define a class called SearchInsertPosition
class SearchInsertPosition:
    # Define a method named searchInsert that takes a list of integers (nums) and an integer (target) as input and returns an integer
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize variables l and r as the left and right indices of the search range respectively
        l, r = 0, len(nums) - 1 
        
        # Perform binary search
        while l <= r:
            # Calculate the mid index of the search range
            mid = (l + r) // 2
            
            # If the target is found at mid index, return mid
            if target == nums[mid]:
                return mid
            # If the target is greater than the element at mid index, update the left index to mid + 1
            if target > nums[mid]:
                l = mid + 1
            # If the target is smaller than the element at mid index, update the right index to mid - 1
            else:
                r = mid - 1
        # If the target is not found, return the final value of the left index which represents the insertion position
        return l

# Create an instance of the SearchInsertPosition class
insert_position = SearchInsertPosition()

# Test cases
nums = [1, 3, 5, 6]
target = 5
results = insert_position.searchInsert(nums, target)
print(results)

nums = [1, 3, 5, 6]
target = 2
results = insert_position.searchInsert(nums, target)
print(results)

nums = [1, 3, 5, 6]
target = 7
results = insert_position.searchInsert(nums, target)
print(results)