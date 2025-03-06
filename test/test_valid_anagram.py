from src.day2.valid_anagram import valid_anagram

def test_valid_anagram():
    assert(valid_anagram("racecar", "carrace")) == True
    assert(valid_anagram("car", "carr")) == False
    assert(valid_anagram("x", "y")) == False
    
    
    
