# Implement your function below.
def is_rotation(list1, list2):
    if (len(list1) != len(list2)):
        return False
    index1, index2 = 0, -1
    elem1 = list1[index1]
    try:
        index2 = list2.index(elem1)
    except:
        return False

    for index in range(len(list1)):
        indexo = (index2+index) % len(list1)
        if list1[index] != list2[indexo]:
            return False
    return True

# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
print(is_rotation(list1, list2a)) # should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
print(is_rotation(list1, list2b)) # should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
print(is_rotation(list1, list2c)) # should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
print(is_rotation(list1, list2d)) # should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
print(is_rotation(list1, list2e)) # should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
print(is_rotation(list1, list2f)) # should return True.
