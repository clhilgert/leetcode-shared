# https://leetcode.com/problems/copy-list-with-random-pointer/description/
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

def copyRandomList(head):
    dummy = Node(float('-inf'))
    curr = head
    new_curr = dummy
    node_dict = {}
    while curr:
        #node we made
        next_node = Node(curr.val)
        new_curr.next = next_node
        node_dict[curr] = next_node
        curr = curr.next
        new_curr = new_curr.next
    curr = head
    new_curr = dummy.next
    while curr:
        if curr.random:
            new_curr.random = node_dict[curr.random]
        curr = curr.next
        new_curr = new_curr.next
    return dummy.next
#{ OldNode(7): NewNode(7), OldNode(13): NewNode(13) }


# d->1->2->3->4
# 1->2->3->4