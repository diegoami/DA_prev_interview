def is_one_away(s1, s2):
    changes = 0
    if len(s1)-len(s2) > 1 or len(s1)-len(s2) < -1:
        return False
    elif len(s1) == len(s2):

        for index in range(len(s1)):
            if s1[index] != s2[index]:
                changes += 1
        return changes <= 1
    else:
        if len(s2) < len(s1):
            s1, s2 = s2, s1
        diff_count = 0
        for index in range(len(s1)):
            if s1[index] != s2[index+diff_count]:
                diff_count += 1

        return diff_count <= 1

# NOTE: The following input values will be used for testing your solution.
print(is_one_away("abcde", "abcd")) # should return True
print(is_one_away("abde", "abcde")) # should return True
print(is_one_away("a", "a"))  # should return True
print(is_one_away("abcdef", "abqdef"))  # should return True
print(is_one_away("abcdef", "abccef"))  # should return True
print(is_one_away("abcdef", "abcde"))  # should return True
print(is_one_away("aaa", "abc"))  # should return False
print(is_one_away("abcde", "abc"))  # should return False
print(is_one_away("abc", "abcde"))  # should return False
print(is_one_away("abc", "bcc"))  # should return False
