def conv_bin(n):
    b = []
    while n >= 1:
        b.append(n % 2)
        n = n // 2
    return (b, len(b))

#print(conv_bin(9))

def tri_bulles(T):
    """
    video tri a bulles: https://www.youtube.com/watch?v=zhODyvOB3SI&t=1s
    """
    n = len(T)
    for i in range(n-1, -1, -1):
        for j in range(i):
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T


print(tri_bulles([2, 3, 6, 7, 1, 4, 2, 8, 0]))


