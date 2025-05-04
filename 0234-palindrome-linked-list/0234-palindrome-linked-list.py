# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        ##finding middle part
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        ## reverse the second part
        prev = 0
        while slow:
            forw = slow.next
            slow.next = prev
            prev = slow
            slow = forw
        
        ## compare the first and second half

        fh = head
        sh = prev

        while sh:
            if fh.val != sh.val:
                return False
            fh = fh.next
            sh = sh.next
        
        return True
            
        