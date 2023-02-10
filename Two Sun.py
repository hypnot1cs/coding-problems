# #! /usr/bin/env python3.11
# Returns the position of 2 int in agiven array, that when added together equals the target int
# By hypnotics; Started on 29/11/22 Completed on 30/11/22 
# File Type: LeetCode Problem @ https://leetcode.com/problems/two-sum/

"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


"""


# class Solution:
#     def twoSum(nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)):
#             if len(nums) == 2:
#                 if nums[i] + nums[i+1] == target:
#                     return [0,1]
#             try:
#                 if nums[i] + nums[i+1] == target:
#                        return [nums.index(nums[i]),nums.index(nums[i+1])]
#             except IndexError:
#                 if nums[0] + nums[i] == target:
#                     return [nums.index(nums[i]),nums.index(nums[i+1])]



def main():
    a = [9,6,6,12,7,6] #targets
    b = [[2,7,11,15],[3,2,4],[3,3],[9,4,5,3],[3,6,4,5],[3,2,3]] #Test cases
    c = [[0,1],[1,2],[0,1],[0,3],[0,2],[0,2]] #Expected results
    # a = [6,6]
    # b = [[3,2,4],[3,3]]
    # c = [[1,2],[0,1]]

    for i in range(len(a)):
        print(Solution.twoSum(target = a[i], nums = b[i]),f"Expected results {c[i]}")



"""
Given an array add all ints till the target is met
Create an array with all values but the value we check 


[2,7,11,15] target value = 9
2 [7,11,15] 2+7, 2+11, 2+15
7 [11,15] 7+11, 7+15
11 + 15

[3,2,4]
3 [2,4] 3+2 3+4
2 + 4

repeat in range of the length of the array -3
at the end of the loop there should be 2 end value 
"""

class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        returned = list(nums)
        if len(returned) == 2: return [0,1]
        a = 0
        while a != len(returned) - 1: #Should we use while instead of for?
            x = nums[0]
            nums.pop(0)
            for i in nums:
                if i + x == target:
                    if i == x:
                        x = returned.index(x)
                        returned.pop(x)
                        y = returned.index(i)
                        return [x,y+1]
                    return [returned.index(x),returned.index(i)]
            a += 1



main()
"""
returned [2, 7, 11, 15]
The nums [7, 11, 15]
X 0
Y1
[0, 1] Expected results [0, 1]

None Expected results [1, 2]

None Expected results [0, 1]

Returned [9, 4, 5, 3]
The nums [4, 5, 3]
X 0
Y3
[0, 3] Expected results [0, 3]

Returned [3, 6, 4, 5]
The nums [6, 4, 5]
X 0
Y2
[0, 2] Expected results [0, 2]
"""
