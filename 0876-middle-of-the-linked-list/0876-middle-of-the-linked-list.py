# Definition for singly-linked list.
import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        cnt = 0
        li = []
        while temp:
            cnt += 1
            temp = temp.next
        
        start = ceil(cnt/2)
        print(start)
        if cnt%2 == 0:
            start += 1
        print(start)
            
        temp = head
        cnt = 0

        while temp:
            cnt += 1
            if cnt == start:
                return temp
            temp = temp.next
            

    
        
                
        