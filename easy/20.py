class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', 
                    '}': '{', 
                    ']': '['}
        
        def isOpenBracket(bracket):
            return bracket in brackets.values()
        
        def isMappedClosedBracket(closedBracket):
            return stack and brackets[closedBracket] == stack[-1]
        
        for bracket in s:
            if isOpenBracket(bracket):
                stack.append(bracket)
            else:
                if isMappedClosedBracket(bracket):
                    stack.pop()
                else:
                    return False
        
        return not stack
        
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

---

# Approach

## Stack
- time complexity: O(n)
- space complexity: O(n)

# Testcase

'((((()))))' -> True (O)
'((()' -> False (O)

"""