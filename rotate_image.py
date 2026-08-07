# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
"""
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Input: matrix = 
[[1,2,3],
[4,5,6],
[7,8,9]]
Output: 
[[7,4,1],
[8,5,2],
[9,6,3]]

"""

# what i can understand about this problem is that we are given an n*n 2D matrix , which we need to rotate 90 degrees clockwise (in-place).

# steps: 1.do the transpose . 2. rotate the list
class Solution():
    def rotate_image(self,matrix:list[list[int]])->list[list[int]]:

        n=len(matrix)
        # 1. Transpose :-                       rows -> columns  and columns -> rows
        for i in range(n):
            for j in range(i+1,n):              # this range is playing a very crucial functin here as we don't want to swap again our already swapped values
                    matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

        # 2. Rotate each row in the matrix 
        for value in matrix:
            value.reverse()


        return matrix            





mat = [[1,2,3],[4,5,6],[7,8,9]]
print(mat)
sol=Solution()
value = sol.rotate_image(mat)        

print(value)

"""
[[00,01,02],          
[10,11,12],   
[20,21,22]]


"""

# In case we are given m*n matrix we cant solve that question in-place : as there would be not sufficient space to fit the transpose

# our code remains same but we have to use another n*m matrix

class Solution2():
    def rotate_irregular_image(self,matrix:list[list[int]])->list[list[int]]:
        m = len(matrix)        # number of rows
        n = len(matrix[0])     # number of columns

        # Step 1: Transpose into a new n×m matrix
        new_matrix = [[0] * m for _ in range(n)]        ## imp
        for i in range(m):
            for j in range(n):
                new_matrix[j][i] = matrix[i][j]

        # Step 2: Reverse each row to complete rotation
        for row in new_matrix:
            row.reverse()

        return new_matrix


mat2 = [[1,2,3],[4,5,6]]
print(mat2)
sol2=Solution2()
print(sol2.rotate_irregular_image(mat2))

### EXTRA
# rotate image 180 degree
class Solution3:
    def rotate_180(self, matrix: list[list[int]]) -> list[list[int]]:
        n = len(matrix)

        # Step 1: Reverse the rows (top ↔ bottom)
        matrix.reverse()

        # Step 2: Reverse each row (left ↔ right)
        for row in matrix:
            row.reverse()

        return matrix


# Example
mat3 = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

sol = Solution3()
print(sol.rotate_180(mat3))
