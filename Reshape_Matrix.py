# Approach 1 : O(m*n) for both tc and sc
class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        # 1. Check if reshaping is mathematically possible
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        # 2. Flatten the original matrix into a 1D list
        flat_matrix = [num for row in mat for num in row]
        
        # 3. Initialize the new empty matrix with r rows and c columns
        new_matrix = [[0] * c for _ in range(r)]
        
        # 4. Fill the new matrix with elements from the flattened list
        k = 0  # Pointer to track our position in the flat_matrix
        for i in range(r):
            for j in range(c):
                new_matrix[i][j] = flat_matrix[k]
                k += 1
                
        return new_matrix

sol = Solution()
print(sol.matrixReshape([[1,2],[4,5]],1,4))

# Approach 2 TC O(m*n) and SC O(1) 
class Solution2:
    def MatrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        total_elements = m * n
        
        # 1. Check if reshaping is mathematically possible
        if total_elements != r * c:
            return mat
            
        # 2. Initialize the new empty matrix
        new_matrix = [[0] * c for _ in range(r)]
        
        # 3. Map directly using division and modulo
        for i in range(total_elements):
            # Find coordinates for the old matrix
            old_row = i // n
            old_col = i % n
            
            # Find coordinates for the new matrix
            new_row = i // c
            new_col = i % c
            
            # Transfer the value
            new_matrix[new_row][new_col] = mat[old_row][old_col]
            
        return new_matrix

sol2 = Solution2()
print(sol2.MatrixReshape([[1,2],[4,5]],1,4))    