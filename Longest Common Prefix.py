# #! /usr/bin/env python3.11
# Finds the longet common prefix of a list of words
# By Hypnotics; Start Date: 25/11/22 Completed: 28/11/22 
# File type: Programming Problem. Full problem can be found @ https://leetcode.com/problems/longest-common-prefix/



"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

"""

def main(intake):
    string = intake[8:]
    #string = string[:len(string)-1]
    string = string.replace('"','')
    string = string.split(',')

class Solution:
    def longestCommonPrefix(strs: list[str]) -> str:
        string = strs[8:]
        string = string[:len(string)-1]
        string = string.replace('"','')
        strs = string.split(',')
        prefix = ''
        if strs[0][0] != strs[1][0]:
            return ""
        else:
            prefix = strs[0][:2]
            num = 0
            for i in strs:
                if i[:2] != prefix:
                    return ""
            while True:
                num_of_loop = 3
                prefix += strs[0][:num_of_loop]
                for i in strs:
                    if prefix != i[:num_of_loop]:
                        return i[:num_of_loop - 1]
                num_of_loop += 1
print(Solution.longestCommonPrefix(strs=input()))



