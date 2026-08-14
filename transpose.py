class Solution(object):
    def transpose(self, matrix):
        
        m=len(matrix)
        n=len(matrix[0])

        # Create a new matrix of size n x m filled with zeros
        res = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(m):
            for j in range(n):
                # The element at [i][j] in the original 
                # goes to [j][i] in the transposed matrix
                res[j][i] = matrix[i][j]

        return res

sol=Solution()
print(sol.transpose([[1,2],[3,4]]))
# tc and sc of O(m*n)