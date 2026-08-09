"""
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 
This matrix has the following properties:

:->Integers in each row are sorted in ascending from left to right.
:->Integers in each column are sorted in ascending from top to bottom
"""

# optimal O(m+n)    {each row is sorted} {but not globally}  # BEST
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:      # i.e, if list and list[list] is empty
            return False

        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1   # start at top-right corner

        while row < rows and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                col -= 1   # move left   {remain in same row}
            else:
                row += 1   # move down   {move to next row }
        return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,20,23,26,30]]
target = 20

sol=Solution()
print(sol.searchMatrix(matrix,target))

""" LET given matrix :-     , and target =21
[
 [1,  4,  7, 11, 15],
 [2,  5,  8, 12, 19],
 [3,  6,  9, 16, 22],
 [10, 13, 14, 17, 24],       
 [18, 21, 23, 26, 30]
]

📊 Trace Table
Iteration (Row,Col)	Value	Action
0	        (0,4)	15	Move Down    15 < 21 row += 1
1	        (1,4)	19	Move Down    19 < 21 row += 1
2	        (2,4)	22	Move Left    22 > 21 col -= 1      # each column is also sorted
3	        (2,3)	16	Move Down    16 < 21 row += 1
4	        (3,3)	17	Move Down    17 < 21 row += 1
5	        (4,3)	26	Move Left    26 > 21 col -= 1
6	        (4,2)	23	Move Left    23 > 21 col -= 1
7	        (4,1)	21	✅ Found

"""

# Appraoch 2   {O(log m + log n).  which is better but}   NOT PREFERRED AS IT HAS SOME EXCEPTIONS
class Solution2:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Edge case: empty matrix or empty row
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])

        # -------------------------------
        # Phase 1: Binary search on rows
        # -------------------------------
        # We try to find a candidate row where the target could lie.
        # Condition: target must be between the first and last element of that row.
        top, bottom = 0, rows - 1
        candidate_row = -1

        while top <= bottom:
            mid = (top + bottom) // 2
            # Check if target lies within the range of this row
            if matrix[mid][0] <= target <= matrix[mid][cols - 1]:         # between this row and col values
                candidate_row = mid
                break
            elif target < matrix[mid][0]:
                # Target is smaller than the first element → move search upward
                bottom = mid - 1
            else:
                # Target is larger than the last element → move search downward
                top = mid + 1

        # If no row satisfies the condition, target cannot exist
        if candidate_row == -1:
            return False

        # -------------------------------
        # Phase 2: Binary search in row
        # -------------------------------
        # Now we search inside the candidate row using standard binary search.
        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[candidate_row][mid] == target:
                return True
            elif matrix[candidate_row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # If not found in candidate row
        return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20

sol2=Solution2()
sol2.searchMatrix(matrix,target)

"""  |^This works only if each row is sorted individually AND the target can belong to exactly one rowz's range.

In LeetCode 240, the matrix is sorted both row-wise and column-wise, so *multiple rows can overlap in value ranges.
so in case our target = 20 and the 1st binary search choses row in which last column value = 22 hoever target not present 
so it will state it false but the target may be present in further rows  """

# Brute force {extra O(m*n)}
class Solution3:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == target :
                    return True
        return False        