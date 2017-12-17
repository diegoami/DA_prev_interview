# Implement your function below.
def is_rotation(list1, list2):
    fol_dict = {}
    for index in range(len(list1)):
        elem1, elem2 = list1[index], list2[index]
        if index == len(list1)-1:
            felem1, felem2 = list1[0], list2[0]
        else:
            felem1, felem2 = list1[index+1], list2[index+1]
        if elem1 in fol_dict:
            if fol_dict[elem1] != felem1:
                return False
        else:
            fol_dict[elem1] = felem1
        if elem2 in fol_dict:
            if fol_dict[elem2] != felem2:
                return False
        else:
            fol_dict[elem2] = felem2

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
