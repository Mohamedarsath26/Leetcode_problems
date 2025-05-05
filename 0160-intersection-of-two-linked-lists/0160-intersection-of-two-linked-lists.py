# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if headA == None or headB == None:
            return None

        t1 = headA
        t2 = headB

        while t1 != t2:
            if t1:
                t1 = t1.next
            else:
                t1 = headB
            if t2:
                t2 = t2.next
            else:
                t2 = headA

            if t1 == t2:
                return t1
        
        return t1