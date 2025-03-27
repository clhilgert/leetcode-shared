# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # self.next = next


def remove_nth_node(head, ind):
    count = 0
    dummy = ListNode(0)
    dummy.next = head
    cur = dummy
    while cur:
        count += 1
        cur = cur.next
    count = count - ind

    cur = dummy
    for _ in range(count - 1):
        cur = cur.next

    cur.next = cur.next.next

    return dummy.next


# without dummy node by chatgpt
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_node(head, ind):
    fast = head
    slow = head

    # Move fast ahead by ind steps
    for _ in range(ind):
        fast = fast.next

    # If fast is None, we're removing the head
    if not fast:
        return head.next

    # Move both fast and slow
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Skip the nth node
    slow.next = slow.next.next

    return head
