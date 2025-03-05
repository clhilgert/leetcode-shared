from src.day1.subsets import subsets

def test_subsets():
    result1 = subsets([1, 2, 3])
    expected1 = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    
    result1 = [sorted(subset) for subset in result1]
    expected1 = [sorted(subset) for subset in expected1]
    
    assert sorted(result1) == sorted(expected1)

    result2 = subsets([0])
    expected2 = [[], [0]]

    result2 = [sorted(subset) for subset in result2]
    expected2 = [sorted(subset) for subset in expected2]
    
    assert sorted(result2) == sorted(expected2)
