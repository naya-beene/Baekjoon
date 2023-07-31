import sys, math
input = sys.stdin.readline

M = 123456 # 문제에서 제공한 M의 범위의 최댓값

arr = [True for _ in range(2 * M + 1)]
arr[0], arr[1] = False, False # 0, 1은 소수가 아니기에  False

# 에라토스테네스의 체 공식
for i in range(2, int(math.sqrt(2 *M) + 1)): # 2부터 int(math.sqrt(2 * 123456)) 까지 반복
    if arr[i]: # 만약 arr[i]가 True(소수)라면
        j = 2 # i에 곱해줄 j값을 2부터 설정 
        while i * j <= 2 * M: # i * j 가 2 * 123456 보다 작거나 같다면
            arr[i * j] = False #해당 i * j 의 값은 소수가 아니므로 False로 설정
            j += 1 # j를 1씩 증가

while True:
    N = int(input())
    if N == 0:
        break
    
    count = 0
    for i in range(N+1, 2*N+1): 
        if arr[i]: # 만약 해당 i가 True(소수) 라면
            count += 1 # count + 1
    print(count)