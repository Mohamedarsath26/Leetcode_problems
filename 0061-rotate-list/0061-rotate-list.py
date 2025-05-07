# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def count(self,head):
        cnt = 0
        temp = head
        while temp:
            cnt += 1
            temp = temp.next
        return cnt
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head  # Handle edge cases

        length = self.count(head)
        
        k = k % length

        if k == 0:
            return head
        stop = self.count(head) - k
        cnt = 0

        temp = head
        org = head

        while temp:
            cnt+=1 
            if cnt == stop:
                next_node = temp.next
                temp.next = None
                new_head = next_node
                tail = new_head
                while tail.next:
                    tail = tail.next
                tail.next = org
            temp = temp.next
        
        return new_head
        