class Solution:
    def minimumTotal(self, triangle):
        """
        1
        2, 3
        4, 5, 6
        7, 8, 9, 10
        From bottom to top strategy

        14(4+7+2+1)
        13(4+7+2), 3
        11(4+7), 5, 6
        7, 8, 9, 10
        """
        N = len(triangle)

        for r in range(N - 2, -1, -1):
            for c in range(r + 1):
                triangle[r][c] += min(triangle[r+1][c], triangle[r+1][c+1])
        return triangle[0][0]
