def selectionsort(A):

    for i in range(len(A)):
        pos = i
        for j in range(i+1,len(A)):
            if A[j] < A[pos]:
                pos = j
        tmp = A[i]
        A[i] = A[pos]
        A[pos] = tmp

A = [3, 5, 8, 9, 6, 2]
print("Orginal Array: ",A)
selectionsort(A)
print("Sorted Array: ",A)