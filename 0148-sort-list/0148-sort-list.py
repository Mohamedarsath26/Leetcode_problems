# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def findmiddle(self,head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def mergeTwolist(self,l1,l2):
        dummy = ListNode(-1)
        temp = dummy

        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
                temp = temp.next
            else:
                temp.next = l2
                l2 = l2.next
                temp = temp.next
            
        if l1:
            temp.next = l1
            l1 = l1.next
            temp = temp.next

        if l2:
            temp.next = l2
            l2 = l2.next
            temp = temp.next
        
        return dummy.next


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head
        
        middle = self.findmiddle(head)
        right = middle.next
        middle.next = None
        left = head

        left = self.sortList(left)
        right = self.sortList(right)

        return self.mergeTwolist(left,right)





        