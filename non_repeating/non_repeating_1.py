# Implement your function below.
def non_repeating(given_string):
    candidates = []
    dups = {}
    for char in given_string:
        if char not in dups:
            dups[char] = 1
            candidates.append(char)
        else:
            dups[char] = dups[char]+1
    for char in candidates:
        if dups[char] <= 1:
            return char
    return None

# NOTE: The following input values will be used for testing your solution.
print(non_repeating("abcab")) # should return 'c'
print(non_repeating("abab")) # should return None
print(non_repeating("aabbbc")) # should return 'c'
print(non_repeating("aabbdbc")) # should return 'd'