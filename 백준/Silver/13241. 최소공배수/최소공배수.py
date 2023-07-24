import sys, math
input = sys.stdin.readline

A, B = map(int, input().split())
print(math.lcm(A, B)) # lcm() : 최소공배수 함수
                      # gcd() : 최대공약수 함수
