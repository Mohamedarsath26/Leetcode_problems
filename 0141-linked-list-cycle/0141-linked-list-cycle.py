# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ls = []
        temp = head
        while temp:
            if temp.val in ls:
                return True
            ls.append(temp.val)
            temp = temp.next
        
        