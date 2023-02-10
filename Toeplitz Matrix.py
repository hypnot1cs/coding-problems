# #! /usr/bin/env python3.11 
# Returns true if all diagonals in a matrix are the same number 
# By Hypnotics; Started on 02/12/22 Completed on 06/12/22
# File Type: LeetCode Problem @ https://leetcode.com/problems/toeplitz-matrix/

"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

Example 1:
TE_EX1
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]

1 2 3 4
5 1 2 3
9 5 1 2

Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:
TE_EX2
Input: matrix = [[1,2],[2,2]]
1 2
2 2
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 20
    0 <= matrix[i][j] <= 99

 

Follow up:

    What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
    What if the matrix is so large that you can only load up a partial row into the memory at once?


move down a row:
Row + 1 Collum +1 
   1 2 3 4

1  1 2 3 4
2  5 1 2 3
3  9 5 1 2

num = 6 + 3
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6
1 2 3 4 5 6


value 1,1 is 1 so value 2,2 would be next in row

Problem:: Find out how to determine the amount of diagonals in a matrix
Number of rows equals number the length of the first row + the number of rows - 1
"""


# class Solution:
#     def isToeplitzMatrix(matrix: list[list[int]]) -> bool:
#         if len(matrix[0]) == 1:
#             return True
#         diagonals = [i for i in matrix[0]] #finds the first set of diagonals
#         diagonals1 = []
#         for i in range(len(matrix)-1): diagonals1.append(matrix[i+1][0]) # finds the second set of diagonals
#         diagonal = [diagonals,diagonals1]
#         verify = []
#         for n in diagonal:
#             for z in n:
#                 loop = 0
#                 index = 0
#                 for c in range(len(matrix)): # Loop to many times 
#                     try:
#                         verify.append(matrix[loop][index])
#                         matrix[loop].pop(matrix[loop].index(matrix[loop][index]))
#                         index += 1
#                         loop += 1
#                     except IndexError:
#                         break
#                 num = 0
#                 for i in verify:
#                     num += int(i)
#                 if int(i) != num // len(verify): 
#                     return False
#                 verify = []
#         return True

# matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# print(Solution.isToeplitzMatrix(matrix=matrix))


"""


[[1,2,3,4],[5,1,2,3],[9,5,1,2]]
"""


"""
0  9  52 22 65 69 13  0 93 17 27 77 99 15
65 0  9  52 22 65 69 13 50 93 17,27 77 99
"""

"""
[[53,64,90,98,34],[91,53,64,90,98],[17,91,53,64,0]]
53 64 90 98 34
91 53 64 90 98
17 91 53 64  0
"""

"""
[[11,74,0,93],[40,11,74,7]]

11 74  0 93
40 11 74  7
"""

class Solution:
    def isToeplitzMatrix(matrix: list[list[int]]) -> bool:
        for i in range(len(matrix[0]) + len(matrix) -1):
            diagonal = []
            for z in range(len(matrix)):
                try:
                    diagonal.append(matrix[z][z])
                    matrix[z].pop(z)
                except IndexError:
                    break
            num = 0
            for c in diagonal:
                num += c
            if diagonal[0] != num / len(diagonal): return False
            if len(matrix[0]) == 0: matrix.pop(0)
        return True

matrix = [[36,59,71,15,26,82,87],[56,36,59,71,15,26,82],[15,56,36,59,71,15,26]]
print(Solution.isToeplitzMatrix(matrix=matrix))
            

"""
1 2 3 4 
5 1 2 3
9 5 1 2

2 3 4
5 2 3
9 5 2

3 4
5 3
9 5

4
5 
9 5

4
9
"""



"""
Trace all the diagonals 
find the sum of the nums and divide by the length of the array
if the average isn't equal to the first num, then return False
else return True
"""

"""
[[36,59,71,15,26,82,87],[56,36,59,71,15,26,82],[15,0,36,59,71,15,26]]

36 59 71 15 26 82 87
56 36 59 71 15 26 82
15  0 36 59 71 15 26



"""
