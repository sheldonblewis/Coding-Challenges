class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        largest = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                square = True
                while square:
                    if j + largest + 1 > len(matrix[0]):
                        break
                    if i + largest + 1 > len(matrix):
                        return largest ** 2
                    for k in range(largest+1):
                        for l in range(largest+1):
                            if matrix[i+k][j+l] == "0":
                                square = False
                                break
                        if square == False:
                            break
                    if square:
                        largest += 1
        
        return largest ** 2
