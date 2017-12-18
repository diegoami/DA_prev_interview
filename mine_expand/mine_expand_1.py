# Implement your function below.
def click(field, num_rows, num_cols, given_i, given_j):
    done = False
    if field[given_i][given_j] == 0:
        field[given_i][given_j] = -2
    else:
        return field
    while not done:
        done = True
        for y in range(num_rows):
            for x in range(num_cols):
                if field[y][x] == -2:
                    yl, yh = max(y-1,0), min(y+1,num_rows-1)
                    xl, xh = max(x-1,0), min(x+1,num_cols-1)
                    for yx in range(yl, yh+1):
                        for xx in range(xl, xh+1):
                            if field[yx][xx] == 0:
                                field[yx][xx] = -2
                                done = False

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
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]

print(click(field1, 3, 5, 2, 2))#
#  should return:
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, -1, 1, 0]]

print(click(field1, 3, 5, 1, 4))
# should return:
# [[-2, -2, -2, -2, -2],
#  [-2, 1, 1, 1, -2],
#  [-2, 1, -1, 1, -2]]


field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

print(click(field2, 4, 4, 0, 1))
#should return:
# [[-1, 1, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 1, 1],
#  [0, 0, 1, -1]]

print(click(field2, 4, 4, 1, 3))
# should return:
# [[-1, 1, -2, -2],
#  [1, 1, -2, -2],
#  [-2, -2, 1, 1],
#  [-2, -2, 1, -1]]
