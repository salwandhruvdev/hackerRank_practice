"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if head is None:
        return False
    visited = []
    next_node = head.next
    
    while next_node != None:
        if next_node in visited:
            return True
        visited.append(next_node)
        next_node = next_node.next
    return False