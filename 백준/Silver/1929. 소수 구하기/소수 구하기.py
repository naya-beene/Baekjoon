import sys, math
input = sys.stdin.readline

M, N = map(int, input().split())
for i in range(M, N+1):
    if i == 1: # 1은 소수가 아니므로 제외
        continue
    for j in range(2, int(i**0.5)+1): # 특정 수의 제곱근을 구해, 그 제곱근까지의 약수 구하기
        if i % j == 0: # 약수가 존재하므로 소수가 아님
            break #  더 이상 검사할 필요가 없으므로 종료
    else:
        print(i)