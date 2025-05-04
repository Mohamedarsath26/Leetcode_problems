# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next is None:
            return None
    
        cnt = 0
        prev = None
        temp = head
        while temp:
            cnt += 1
            temp = temp.next

        if cnt == n:
            return head.next
        
        temp = head
        
        while temp:
            if cnt == n:
                prev.next = prev.next.next
            prev = temp
            temp = temp.next
            cnt-=1
        
        return head
        