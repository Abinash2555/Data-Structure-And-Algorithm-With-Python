def calculate_rec(n):
    if  n > 0: #Base case
        calculate_rec(n - 1)
        k = n ** 2
        print(k)



calculate_rec(4)