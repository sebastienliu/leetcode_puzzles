class Solution:
    def reshape(self, mat, r, c):
        N, M = len(mat), len(mat[0])
        T = r * c
        if N * M != T:
            return mat

        newMatrix = list()
        sC = 0
        sR = 0
        for i in range(N):
            for j in range(M):
                if sC == c:
                    sR += 1
                    sC = 0
                newMatrix.append(mat[i][j])
                sC += 1
        return [newMatrix]
