# Definition for singly-linked list.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class MergeTwoSortedLists:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2  # Efficiently append remaining elements

        # Print the merged linked list
        current = dummy.next
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

        return dummy.next

mergeSort = MergeTwoSortedLists()

# Create linked lists from the given lists
def create_linked_list(lst):
    dummy = ListNode()
    tail = dummy
    for val in lst:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

list1 = [1, 2, 4]
list2 = [1, 3, 4]
l1 = create_linked_list(list1)
l2 = create_linked_list(list2)
results = mergeSort.mergeTwoLists(l1, l2)
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> None

list1 = []
list2 = [0]
l1 = create_linked_list(list1)
l2 = create_linked_list(list2)
results = mergeSort.mergeTwoLists(l1, l2)
# Output: 0 -> None

list1 = []
list2 = [0]
l1 = create_linked_list(list1)
l2 = create_linked_list(list2)
results = mergeSort.mergeTwoLists(l1, l2)
# Output: 0 -> None