# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = None
        head = None

        while list1 or list2:
            node = None
            if not list1:
                node = list2
                list2 = list2.next
            elif not list2:
                node = list1
                list1 = list1.next
            elif list1.val >= list2.val:
                node = list2
                list2 = list2.next
            else:
                node = list1
                list1 = list1.next

            if not list3:
                list3 = node
                head = list3
            else:
                list3.next = node
                list3 = list3.next
        return head
        