# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev = None
        temp = head
        while temp:
            forw = temp.next
            temp.next = prev
            prev = temp
            temp = forw
        return prev

    def count_nodes(self,head):
        cnt = 0
        temp = head
        while temp:
            cnt+=1
            temp = temp.next
        return cnt
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        dummy = None
        kth = 0
        final_head = None
        prev_node = None

        total_node = self.count_nodes(temp)

        while temp and total_node >= k:
            if dummy == None:
                dummy = temp
            kth += 1
            if kth == k:
                next_node = temp.next ## store the next node
                temp.next = None
                new_head = self.reverse(dummy)
                if final_head is None:
                    final_head = new_head
                if prev_node:
                    prev_node.next = new_head

                prev_node = dummy # for track of the last node of reversed
                temp = next_node 
                dummy = temp
                kth = 0
                total_node -= k
            else:
                temp = temp.next

        if prev_node: ## if still nodes are there
            prev_node.next = temp

        return final_head
            

            

        