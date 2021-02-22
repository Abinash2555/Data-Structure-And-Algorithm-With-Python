def insertionsort(A):
    n = len(A)
    for i in range(1,n):
        cvalue = A[i]
        postion = i
        while postion > 0 and A[postion - 1] > cvalue:
            A[postion] = A[postion-1]
            postion = postion - 1

        A[postion] = cvalue

A = [3, 5, 8, 9, 6, 2]
print("Orginal Array: ",A)
insertionsort(A)
print("Sorted Array: ",A)



