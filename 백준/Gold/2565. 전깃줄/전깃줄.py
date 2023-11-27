import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    A, B = list(map(int, input().split()))
    arr.append((A, B))

arr.sort() # a 전봇대 오름차순 정렬
dp = [1 for _ in range(N)] 
for i in range(N): # b 전봇대의 가장 긴 증가하는 부분 수열 구하기
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp)) # 전체 값에서 가장 긴 증가하는 수열 값을 빼줌