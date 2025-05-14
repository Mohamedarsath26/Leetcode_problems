
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def insert_copy_node(self,head):
        ## copy the nodes in place
        temp = head

        while temp:
            copynode = Node(temp.val)

            next_node = temp.next

            copynode.next = next_node

            temp.next = copynode

            temp = next_node
    
    def connect_random(self,head):
        temp = head

        while temp:

            copy_node = temp.next

            if temp.random:
                copy_node.random = temp.random.next
            else:
                copy_node.random = None
        
            temp = temp.next.next
    
    def extract_only_copy_node(self,head):
        temp = head

        dummynode = Node(-1)

        res = dummynode

        while temp:
            
            copy_node = temp.next # copy node
            res.next = copy_node

            temp.next = temp.next.next ## convert to original ll

            temp = temp.next

            res = res.next

        return dummynode.next
            


    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
       

        if not head:
            return None
        
        self.insert_copy_node(head)

        self.connect_random(head)

        return self.extract_only_copy_node(head)