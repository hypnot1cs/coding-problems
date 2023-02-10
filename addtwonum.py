# #! /usr/bin/env python3.11
# Reverses 2 lists and adds the converted value as it's own list
# By Hypnotics; Started on Completed on
# File Type: Leetcode Problem @ https://leetcode.com/problems/add-two-numbers/

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""

# Definition for singly-linked list.
# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def ListToNode(node: ListNode):
        l = []
        while node:
            l.append(node.val)
            node = node.next
        return l

    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        l1 = Solution.ListToNode(node = l1)
        l2 = Solution.ListToNode(node = l2)
        l1.reverse()
        l2.reverse()
        lists = []
        for i in (l1,l2):
            num = ''
            for z in i:
                num += str(z)
            lists.append(num)
        endValue = int(lists[0]) + int(lists[1])
        endLists = [int(i) for i in str(endValue)]
        endLists.reverse()
        string = ''
        for c in endLists:
            string += f'{c},'
        return ListNode(string[:-1])
        
        
        

