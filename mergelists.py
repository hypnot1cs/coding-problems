# #! /usr/bin/env python3.11
# Adds and Sorts two lists
# By hypnotics; Started on 8/12/22 Completed on 8/12/22
# File Type: Leetcode Problem @ https://leetcode.com/problems/add-two-numbers/

# Results
# Runtime: 36 ms, faster than 95.92% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.9 MB, less than 80.21% of Python3 online submissions for Merge Two Sorted Lists.

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

"""

# class Solution:
#     def mergeTwoLists(list1: list = [], list2: list = []) -> list:
#         for i in list2: list1.append(i)
#         list1.sort()
#         return list1
#



# Definition for singly-linked list.
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
    
    def mergeTwoLists(self,list1: ListNode, list2: ListNode) -> ListNode:
        
        list1 = Solution.ListToNode(node= list1)
        list2 = Solution.ListToNode(node= list2)
        for i in list2: list1.append(i)
        list1.sort()
        string = ""
        for i in range(len(list1)): string += f'{list1[i]},'
        return ListNode(string[:-1])
# print(Solution.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]))



