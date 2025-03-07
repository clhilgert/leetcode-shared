from src.day3.valid_parentheses import valid_parentheses

def test():
    assert valid_parentheses("(") == False
    assert valid_parentheses("[") == False
    assert valid_parentheses("{") == False
    assert valid_parentheses("()") == True
    assert valid_parentheses("({})") == True
    assert valid_parentheses("({[]})") == True  # <--
    assert valid_parentheses("({[])}") == False  # <--
    assert valid_parentheses("({") == False
    assert valid_parentheses("(]") == False
    assert valid_parentheses("]") == False