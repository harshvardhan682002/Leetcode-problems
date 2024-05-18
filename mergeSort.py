# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
from typing import List
class mergeSort:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges array nums2 into nums1 in-place.
        """
        last = m + n - 1  # Index of the last element in the merged array

        m -= 1  # Convert m to be the last index of the initial part of nums1
        n -= 1  # Convert n to be the last index of nums2

        # Merge in reverse order
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[last] = nums1[m]
                m -= 1
            else:
                nums1[last] = nums2[n]
                n -= 1
            last -= 1

        # Fill nums1 with remaining nums2 elements, if any
        while n >= 0:
            nums1[last] = nums2[n]
            n -= 1
            last -= 1
merge_sort = mergeSort()
nums1 = [1,2,3,0,0,0]
m = 3 
nums2 = [2,5,6]
n = 3
merge_sort.merge(nums1, m, nums2, n)
print(nums1)  # Output should be [1, 2, 2, 3, 5, 6]
nums1 = [1]
m = 1 
nums2 = []
n = 0
merge_sort.merge(nums1, m, nums2, n)
print(nums1) # output should be [1]
nums1 = [0]
m = 0 
nums2 = [1]
n = 1
merge_sort.merge(nums1, m, nums2, n)
print(nums1) # output should be [1]