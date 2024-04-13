def comb(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return comb(n-1, k-1) + comb(n-1, k)
    
n = int(input())
k = int(input())

print(comb(n,k))