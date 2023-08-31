import sys
input = sys.stdin.readline
# import math 후 math.factorial 사용가능 
def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

# mCn 으로 표현할 수 있고 이는 m! 을 (m-n)!n! 으로 나눈 값이다.
T = int(input())
for _ in range(T):
    N, M= map(int, input().split())
    bridge = factorial(M) // (factorial(N) * factorial(M - N))
    print(bridge)