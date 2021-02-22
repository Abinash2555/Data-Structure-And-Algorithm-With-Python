def linear_search(A, key):
    index = 0
    while index < len(A):
        if A[index] == key:
            return index

        index += 1
    return -1

A=[84,21, 17, 96, 15]

found = linear_search(A, 15)
print('Result: ', found)

