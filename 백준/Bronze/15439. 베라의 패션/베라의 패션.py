import sys
input = sys.stdin.readline

N = int(input())
result = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if not i == j:
            result = i * j
print(result)