from src.day4.group_anagrams import groupAnagrams

def test_group_anagrams():
    print(sorted(groupAnagrams(["eat","tea","tan","ate","nat","bat"])))
    assert(sorted(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))) == [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']]
    assert(groupAnagrams([""])) == [[""]]
    assert(groupAnagrams(["a"])) == [["a"]]
