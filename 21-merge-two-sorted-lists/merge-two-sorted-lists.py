# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        listR = ListNode()
        l = listR
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                l.next = ListNode(list1.val)
                l = l.next
                list1 = list1.next
            else:
                l.next = ListNode(list2.val)
                l = l.next
                list2 = list2.next
        if list1 == None:
            l.next = list2
        if list2 == None:
            l.next = list1
        return listR.next