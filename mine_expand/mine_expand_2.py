# Implement your function below.
def click(field, num_rows, num_cols, given_i, given_j):
    done = False
    Q = []
    V = set()
    Q.append((given_i,given_j))
    while len(Q) > 0:
        ci, cj = Q.pop(0)
        if (field[ci][cj] == 0):
            field[ci][cj] = -2
            V.add((ci,cj))
            il, ih = max(ci-1,0), min(ci+1, num_rows-1)
            jl, jh = max(cj-1,0), min(cj+1, num_cols-1)
            for yx in range(il, ih+1):
                for xx in range(jl, jh+1):
                    if (yx,xx) not in V:
                        Q.append((yx,xx))

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
