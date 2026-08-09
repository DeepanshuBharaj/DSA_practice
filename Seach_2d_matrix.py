# LeetCode 74: Search a 2D Matrix (Medium)
"""
You are given an m x n integer matrix with the following two properties:

:-> Each row is sorted in non-decreasing order.
:-> The first integer of each row is greater than the last integer of the previous row.
:-> Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""
# APPROACH 1. O(m*n)  not sufficient as we need O(log(m*n))
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)  #rows
        n = len(matrix[0])  # cols
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13      
sol = Solution()
print(sol.searchMatrix(matrix,target))   

# APPROACH 2. *Flattened Binary Search {works for sorted matrix/list} O(log(m * n)) Best for a sorted matrix 
class Solution2:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # base case for []:- empty matrix and [[]] empty matrix[0]
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        
        left, right = 0, rows * cols - 1

        while left <= right:
            mid_index = left + (right - left) // 2

            # convert 1D flattened index → 2D coordinates     {to remember}
            row = mid_index // cols
            col = mid_index % cols
            
            mid_val = matrix[row][col]   # ✅ keep value separate from mid {index}

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid_index + 1
            else:
                right = mid_index - 1

        return False
   

matrix = [[1,3,5,7],[10,13,16,20],[23,30,34,60]]
target = 13      
sol2 = Solution2()
print(sol2.searchMatrix(matrix,target))