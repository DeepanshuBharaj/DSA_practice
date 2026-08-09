#Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

#You must do it in place.

# 1. Set Based Approach O(m*n) tc  :-> efficient but O(m+n) space complexity


# LOGIC :
"""
1.Scan the matrix once
Record all rows and columns that contain at least one 0.
This is done using two sets: zero_rows and zero_cols.

2.Second pass
For each element in the matrix, check if its row or column is marked.
If yes, set it to 0.

👉 This avoids placeholders and repeated work — everything is marked first, then updated in one clean pass.
TC.= O(rows * cols)
SC.= O(rows + cols)
"""
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        # Step 1: Record which rows and cols need to be zeroed
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        print(zero_rows ,"rows are to be set zero")    
        print(zero_cols ,"cols are to be set zero")     

        # Step 2: Zero out recorded rows and cols
        for i in range(rows):
            for j in range(cols):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0


# Example
mat = [[1, 2, 3,10],
       [4, 0, 6,11],
       [7, 8, 9,0]]

print("Before:", mat)
sol = Solution()
sol.setZeroes(mat)
print("After:", mat)


# OPTIMAL SOLUTION :- TC: O(rows.cols)  and SC : O(1) i.e. in-place

class Solution2:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        # returns bool
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Step 1: Use first row and col as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 2: Zero out cells based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: Handle first row
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Step 4: Handle first column
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0


# Example
mat = [[1, 2, 3],
       [4, 0, 6],
       [7, 8, 9]]

print("Before:", mat)
sol = Solution2()
sol.setZeroes(mat)
print("After:", mat)


# Logic :- for why first row and column are excluded and handled separately:-
"""
so let matrix=[[1,2,3]
               [4,0,6]
               [7,8,9]]

we exclude the 1st row and column as  we want them as a marker 
if we include them too

# Step 2: Zero out cells based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

Then in this step if range(0,rows) and (o,cols)  then we have already assigned zero to the 
first values of rows and columns containing zero
AS a result their respective row and colum will also be set to 0 which is not what we want.
therefore , first row and column are handled separately      
"""