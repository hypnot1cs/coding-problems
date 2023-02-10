# #! /usr/bin/env python3.11
# Returns a bool based on valid parathaseas syntax
# By Hypnotics; Started Completed 
# File Type: LeetCode Problem @ https://leetcode.com/problems/valid-parentheses/

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

"""

def main():
    test_cases = ['(){}}{']
    expected = [False]
    for i in range(len(test_cases)):
        print(f"Results {Solution.valid(test_cases[i])}\nExpected {expected[i]}")

class Solution:
    def valid(s: list) -> bool:
        if len(s) == 1: return False
        def opposite(value: str) -> str:
            if value == str('('): return str(')')
            if value == str('{'): return str('}')
            if value == str("["): return str("]")
        unclosed = []
        expected = ''
        for i in s:
            if i in ("(","[","{"): 
                unclosed.append(i)
                expected = opposite(i)
            elif i != expected:
                return False
            if i == expected: 
                try:
                    unclosed.pop(len(unclosed)-1)
                except IndexError:
                    return False
                if len(unclosed) > 0:
                    expected = opposite(unclosed[len(unclosed)-1])
        if len(unclosed) > 0: return False
        else: return True

        

            


"""
Get a value, we need to find out if the value has closed
Get a oppeneing value, expected value is the closing value but, if a clossing value is unexpected retrun False, else return True

"""

main()
