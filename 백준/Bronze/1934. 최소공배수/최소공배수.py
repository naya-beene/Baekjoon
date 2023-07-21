import sys, math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(math.lcm(A, B)) # lcm() : 최소공배수 함수
                          # gcd() : 최대공약수 함수
