def reverse_ll(head):
    # prev pointer, next pointer, current pointer
    # sever connection to the next node, but we need to store that pointer
    # we set the current node's next pointer to be the previous node
    # set the current pointer to be the next pointer

    prev = None
    curr = head
    next = None

    # iterate down the linked list 
    '''
    
      None -- 1 -- 2 -- 3 
         p   <  p  -- n      
    '''
    while curr:
        next = curr.next # we could cheat and use the python way to swap
        curr.next = prev # 
        prev = curr
        curr = next
        prev, curr.next, curr = curr, prev, curr.next
        
    return prev