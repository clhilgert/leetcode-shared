from src.day4.product_of_array_except_self import productExceptSelf

def test_product_except_self_positive_numbers():
    # Test with positive integers
    nums = [1, 2, 3, 4]
    expected = [24, 12, 8, 6]
    assert productExceptSelf(nums) == expected

def test_product_except_self_with_zeros():
    # Test with a single zero - everything except that position should be 0
    nums = [1, 2, 0, 4]
    expected = [0, 0, 8, 0]
    assert productExceptSelf(nums) == expected
    
    # Test with multiple zeros - all positions should be 0
    nums = [1, 0, 3, 0]
    expected = [0, 0, 0, 0]
    assert productExceptSelf(nums) == expected

def test_product_except_self_negative_numbers():
    # Test with negative numbers
    nums = [-1, -2, -3, -4]
    expected = [-24, -12, -8, -6]
    assert productExceptSelf(nums) == expected
    
    # Test with mixed positive and negative numbers
    nums = [-1, 2, -3, 4]
    expected = [-24, 12, -8, 6] 
    assert productExceptSelf(nums) == expected

def test_product_except_self_edge_cases():
    # Test with single element array (technically not a valid case)
    nums = [5]
    expected = [1]  # No other elements, so product is 1
    assert productExceptSelf(nums) == expected
    
    # Test with two elements
    nums = [2, 3]
    expected = [3, 2]
    assert productExceptSelf(nums) == expected
    
    # Test with empty array (technically not a valid case)
    nums = []
    expected = []
    assert productExceptSelf(nums) == expected

def test_product_except_self_ones():
    # Test with ones
    nums = [1, 1, 1, 1]
    expected = [1, 1, 1, 1]
    assert productExceptSelf(nums) == expected

def test_product_except_self_large_numbers():
    # Test with large numbers
    nums = [10, 20, 30, 40]
    expected = [24000, 12000, 8000, 6000]
    assert productExceptSelf(nums) == expected