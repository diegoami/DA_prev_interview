# Implement your function below.
def mine_sweeper(bombs, num_rows, num_cols):
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    for y,x in bombs:
        field[y][x] = -1
        yl, yh = max(y-1,0), min(y+1, num_rows-1)
        xl, xh = max(x-1, 0), min(x + 1, num_cols - 1)
        for yx in range(yl, yh+1):
            for xx in range(xl, xh+1):
                if field[yx][xx]  != -1:
                    field[yx][xx] += 1

    return field


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
print(mine_sweeper([[0, 2], [2, 0]], 3, 3))
# should return:
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]

print(mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4))
# should return:
# [[-1, -1, 2, 1],
#  [2, 3, -1, 1],
#  [0, 1, 1, 1]]

print(mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5))
#should return:
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]