# -*- coding: utf-8 -*-


def aa(matrix, target):
    m, n = len(matrix), len(matrix[0])
    i, j = m-1, 0
   
    while i >= 0 and j < n:
          if matrix[i][j] == target:
              return True
          elif matrix[i][j] < target:
              j += 1
          else:
              i -= 1
    return False


if __name__ == "__main__":
    print aa([[1,4,7,11,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24], [18,21,23,26,30]], 5)
    print aa([[1,4,7,11,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24], [18,21,23,26,30]], 20)
