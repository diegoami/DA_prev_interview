import copy


# Implement your function below.
# n = # rows = # columns in the given 2d array
def rotate(given_array, n):
    rotated = copy.deepcopy(given_array)
    nn = n - 1
    for y in range(n):
        for x in range(n):
            yv,xv = (y-(n-1)/2, x-(n-1)/2)

            nyv, nxv = xv, -yv
            ny, nx = int(nyv+(n-1)/2), int(nxv+(n-1)/2)
            rotated[ny][nx] = given_array[y][x]
    return rotated


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
a1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
print(rotate(a1, 3)) # should return:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

a2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
print(rotate(a2, 4)) # should return:
# [[13, 9, 5, 1],
#  [14, 10, 6, 2],
#  [15, 11, 7, 3],
#  [16, 12, 8, 4]]
