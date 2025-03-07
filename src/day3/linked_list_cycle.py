# https://leetcode.com/problems/linked-list-cycle/description/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head) -> bool:
    if not head or not head.next:
        return False
    slow = head
    fast = head.next
    while fast.next and fast.next.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False
