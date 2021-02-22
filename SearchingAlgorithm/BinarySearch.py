# def binary_iter(A, key):
#     left = 0
#     Right = len(A) - 1
#     while left <= Right:
#         mid = (Right + 1)//2
#         if A[mid]== key:
#             return mid
#         elif A[mid] < key:
#             left = mid - 1
#
#         elif A[mid] > key:
#             right = mid + 1
#
#     return -1
#
# A = [2, 3, 4, 5, 6, 7]
# # print(len(A))
# found = binary_iter(A, 6)
# print("Found at: ", found)

## Recursive
def binary_rec(A, key, L, R):
    if L > R:
        return -1
    else:
        mid = (1 + R)//2
        if A[mid] == key:
            return mid
        elif key > A[mid]:
            return binary_rec(A, key, mid + 1, R)
        elif key < A[mid]:
            return binary_rec(A, key, L, mid - 1)

A = [12, 14, 20, 22, 28, 32]
result = binary_rec(A, 20, 0, 5)
print ("Result: ", result)



