class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matx = [[0 for _ in range(n)] for _ in range(m)]
        # print(matx)
        for i in indices:
            row = i[0]
            col = i[1]
            for c in range(len(matx[row])):
                matx[row][c] += 1
                # print(matx, 1)
            for m in range(len(matx)):
                matx[m][col] += 1
                # print(matx, 2)
        # print(matx, "f")
        count = 0
        for r in matx:
            for x in r:
                if x % 2 != 0:
                    count += 1
        return count