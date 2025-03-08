# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeTwoLists(list1, list2):
    '''
    // set two pointers to be list1 and list2
    set up a dummy node to return out
    as we iterate over both list1 and list2, we compare the values at each node and add to the dummy node's tail
    at the end, we will have remaining nodes in list1 or list2
    while either of those 2 pointers are pointing to nodes, we add that to the dummy node

    return out 
    
    
    '''
    returned_head = ListNode(-1, None)
    dummy = returned_head

    while list1 and list2:
        if list1.val <= list2.val:
            dummy.next = list1
            # advance pointers
            list1 = list1.next
            dummy = dummy.next 
        else:
            dummy.next = list2
            list2 = list2.next
            dummy = dummy.next # fix duplicate code
    # by this block, we have either list 1 or either list2 and empty out the remaining nodes
    while list1:
        dummy.next = list1
        list1 = list1.next
        dummy = dummy.next

    while list2:
        dummy.next = list2
        list2 = list2.next
        dummy = dummy.next
            
    return returned_head.next



    