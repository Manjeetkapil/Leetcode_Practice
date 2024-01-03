class Solution:
    def setZero(self,i,j,matrix):
        for k in range(0,len(matrix)):
            matrix[k][j] = 0
        for k in range(0, len(matrix[i])):
            matrix[i][k] = 0
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flag = []
        for i in range(0,len(matrix)):
            row = []
            for j in range(0,len(matrix[i])):
                if matrix[i][j]==0:
                    row.append(0)
                else:
                    row.append(-1)
            flag.append(row)
        for i in range(0,len(flag)):
            for j in range(0,len(flag[i])):
                if flag[i][j] == 0:
                    self.setZero(i,j,matrix)
        print(matrix)