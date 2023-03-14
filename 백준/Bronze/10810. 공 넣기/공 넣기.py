import sys
N, M = map(int, sys.stdin.readline().split())
basket = [0] * (N+1)

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for n in range(i, j +1):
        basket[n] = k

for i in range(1, N+1):
    print(basket[i], end=' ')