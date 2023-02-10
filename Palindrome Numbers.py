# #! /usr/bin/env python3.11
# Find the palindrome of a number
# By Hypnotics; Start Date 28/11/22 Completed on: 28/11/22 
# File Type: Leetcode Problem; Problem @ https://leetcode.com/problems/palindrome-number/

"""
Given an integer x, return true if x is a palindrome, and false otherwise.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Input: x = 1000021
Output: False 

Constraints:

    -231 <= x <= 231 - 1


x = 100001; True
x = 1001001; True
"""



class Solution:
    def isPalindrome(x: int) -> bool:
        pal = str(x)
        pal2 = list(pal[len(pal)//2:])
        if len(pal) % 2 == 1: 
            pal2.remove(pal2[0])
        pal2 = list(reversed(pal2))
        string = ''
        for i in pal2:  string += str(i)
        if pal[:len(pal)//2] == string: 
            return True
        else: return False

print(Solution.isPalindrome(x=11))
        
