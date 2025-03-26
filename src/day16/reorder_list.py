# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# https://leetcode.com/problems/reorder-list/description/

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]


def reorderList(head):
    slow, fast = head, head

    # iterate to middle of linked list

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # slow pointer should be at midpoint
    # reverse the back half of the linked list

    cur = slow.next
    prev = None

    # bisect list
    slow.next = None

    while cur:
        nextt = cur.next  # store 5
        cur.next = prev  # point to None
        prev = cur  # prev = 4
        cur = nextt  # cur is now 5

    # interweave two lists
    # at end, rev list will be stored in prev pointer

    head2 = prev

    dummy = ListNode(-1, None)
    curr = dummy

    while head and head2:
        curr.next = head
        curr.next.next = head2

        head = head.next
        head2 = head2.next

    if head:
        curr.next = head

    return dummy.next
