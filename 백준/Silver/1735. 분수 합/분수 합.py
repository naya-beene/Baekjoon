import sys, math
input = sys.stdin.readline

A, B = map(int, input().split())
C, D = map(int, input().split())

bunja, bunmo = A * D + C * B, B * D

gcd = math.gcd(bunja, bunmo) # 분자 분모의 최대공약수를 구한후 나눠줌 
bunja //= gcd                # gcd : 최대공약수 구하는 함수
bunmo //= gcd

print(bunja, bunmo)