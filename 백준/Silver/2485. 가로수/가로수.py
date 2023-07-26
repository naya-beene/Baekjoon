import sys, math
input = sys.stdin.readline

# 이미 심어져있는 가로수 수
N = int(input())

# 첫 가로수 위치
A = int(input())

# 가로수들 사이값 저장할 배열
arr = []

# 가로수 사이의 간격 저장
for i in range(N-1):
    num = int(input())
    arr.append(num - A)
    A = num

# arr에 들어있는 모든 수들의 최대공약수 찾기
g = arr[0]
for j in range(1, len(arr)):
    g = math.gcd(g, arr[j])

# 사이에 심을 가로수 개수: 간격 // 최대공약수 - 1
result = 0
for each in arr:
    result += each // g - 1
print(result)