# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        t1 = l1
        t2 = l2
        quot = 0
        prev = None
        
        while t1 and t2:
            val = t1.val + t2.val + quot
            t1.val = val%10
            quot = val//10
            
            prev = t1
            t1 = t1.next
            t2 = t2.next

        if t2:
            prev.next = t2
            t1 = t2


        ## if any value remain in t1
        while t1:
            val = t1.val + quot
            t1.val = val%10
            quot = val//10

            prev = t1
            t1 = t1.next


        if quot:
            prev.next = ListNode(quot)

        return l1



        