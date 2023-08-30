import sys
input = sys.stdin.readline
# 팩토리얼: 이항계수 정의 이용
N, K= map(int, input().split())

result = 1
for i in range(K):
    result *= N
    N -= 1
    
divisor = 1
for i in range(2, K+1):
    divisor *= i

print(result // divisor)