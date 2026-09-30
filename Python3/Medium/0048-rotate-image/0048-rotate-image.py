class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res: list = []

        res = list(zip(*matrix[::-1]))
        matrix[0:] = res
