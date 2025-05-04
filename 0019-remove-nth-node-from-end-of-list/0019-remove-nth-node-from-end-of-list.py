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

        # First pass: count total nodes
        while temp:
            cnt += 1
            temp = temp.next

        # If the node to delete is the head
        if cnt == n:
            return head.next
        
        temp = head

        # Second pass: move to (cnt - n)th node
        while temp:
            if cnt == n:
                # prev is guaranteed to not be None here
                prev.next = prev.next.next
                  # Node deleted, exit loop
            prev = temp
            temp = temp.next
            cnt -= 1
        
        return head
