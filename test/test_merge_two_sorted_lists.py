from src.day4.merge_two_sorted_lists import mergeTwoLists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list_to_list(node):
    """Convert linked list to a regular list for easier debugging"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test_merge_two_sorted_lists():
    # Test case 1: Sequential lists
    n1 = ListNode(1, ListNode(2, ListNode(3, None)))
    n2 = ListNode(4, ListNode(5, ListNode(6, None)))
    expected = [1, 2, 3, 4, 5, 6]
    assert linked_list_to_list(mergeTwoLists(n1, n2)) == expected

    # Test case 2: Interleaved lists
    n3 = ListNode(1, ListNode(3, ListNode(5, None)))
    n4 = ListNode(2, ListNode(4, ListNode(6, None)))
    assert linked_list_to_list(mergeTwoLists(n3, n4)) == expected

    # Test case 3: Different lengths
    n5 = ListNode(1, ListNode(3, ListNode(5, None)))
    n6 = ListNode(2, ListNode(4, None))
    expected2 = [1, 2, 3, 4, 5]
    assert linked_list_to_list(mergeTwoLists(n5, n6)) == expected2

    # Test case 4: Different lengths reversed
    n7 = ListNode(1, ListNode(3, None))
    n8 = ListNode(2, ListNode(4, ListNode(5, None)))
    assert linked_list_to_list(mergeTwoLists(n7, n8)) == expected2

    # Test case 5: Empty lists
    assert mergeTwoLists(None, None) is None
    
    # Test case 6: One empty list
    n9 = ListNode(1, ListNode(2, ListNode(3, None)))
    expected3 = [1, 2, 3]
    assert linked_list_to_list(mergeTwoLists(n9, None)) == expected3
    assert linked_list_to_list(mergeTwoLists(None, n9)) == expected3
    
    # Test case 7: Lists with duplicate values
    n10 = ListNode(1, ListNode(2, ListNode(3, None)))
    n11 = ListNode(1, ListNode(2, ListNode(3, None)))
    expected4 = [1, 1, 2, 2, 3, 3]
    assert linked_list_to_list(mergeTwoLists(n10, n11)) == expected4
