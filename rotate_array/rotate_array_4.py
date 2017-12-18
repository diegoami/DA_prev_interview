import copy
from math import floor, ceil


# Implement your function below.
# n = # rows = # columns in the given 2d array
def rotate(given_array, n):
    def get_new_pos(y,x,a):
        ny1, nx1, p1  = x  , n-1-y  , a[y][x]
        ny2, nx2, p2  = nx1, n-1-ny1, a[ny1][nx1]
        ny3, nx3, p3  = nx2, n-1-ny2, a[ny2][nx2]
        ny4, nx4, p4  = nx3, n-1-ny3, a[ny3][nx3]
        return [(ny1, nx1, p1),(ny2, nx2, p2),(ny3, nx3, p3),(ny4, nx4, p4)]

    for y in range(floor(n/2)):
        for x in range(ceil(n/2)):
            newpos_s = get_new_pos(y,x,given_array)
            for ny, nx, p in newpos_s:
                given_array[ny][nx] = p
    return given_array


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
