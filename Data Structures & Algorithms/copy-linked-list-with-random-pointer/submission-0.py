"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
    
        h = {}
        t = head

        while t:
            h[t] = Node(t.val)
            t = t.next
  
        t = head
        while t:
            h[t].next = h.get(t.next)
            h[t].random = h.get(t.random)
            t = t.next
    
        return h[head]

            
            