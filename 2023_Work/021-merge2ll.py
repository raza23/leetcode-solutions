class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next