# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge_sorted = ListNode()
        merge_sorted_pointer = merge_sorted
        while list1 is not None or list2 is not None:
            if list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    merge_sorted_pointer.next = ListNode(list1.val)
                    merge_sorted_pointer = merge_sorted_pointer.next
                    list1 = list1.next
                else:
                    merge_sorted_pointer.next = ListNode(list2.val)
                    merge_sorted_pointer = merge_sorted_pointer.next
                    list2 = list2.next
            elif list1 is not None:
                merge_sorted_pointer.next = ListNode(list1.val)
                merge_sorted_pointer = merge_sorted_pointer.next
                list1 = list1.next
            else:
                merge_sorted_pointer.next = ListNode(list2.val)
                merge_sorted_pointer = merge_sorted_pointer.next
                list2 = list2.next

        return merge_sorted.next