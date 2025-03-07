# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true


# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.





def valid_parentheses(str):
    # use a stack here
    # pair the open and closing parentheses in a map / dictionary
    # open pareenthesis means we push elements onto the stack
    # as soon as we see the first closing, we must make sure as we pop off hte stack that they are matching in order
    """
    ({[]})
         ^ if stack length is zero we return True, it's valid
          if the stack length is positive by the time we get to the end itss false


    """
    pairs = {
        "}": "{",
        "]": "[",
        ")": "("
    }

    stack = []
    # "[)"

    for char in str:
        if char in pairs: # we are grabbing all closing parenthesi
            # if values are not equal i can immediatley return false
            if not stack or pairs[char] != stack[-1]:
                return False
            stack.pop()
        else:
            stack.append(char) # enforcing only open parenthesis go on the stack  ["("]
    
    return False if len(stack) > 0 else True
        