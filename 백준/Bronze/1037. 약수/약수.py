import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
if A != 1 and A != N:
    print(max(A) * min(A))