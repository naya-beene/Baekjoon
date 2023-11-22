import sys
input = sys.stdin.readline

A = int(input()) # 수열의 크기
s = list(map(int, input().split())) # 수열 리스트
dp = [1] * A # A = 6, dp=[1, 1, 1, 1, 1, 1]

for i in range(1, A): 
    for j in range(i):
        if s[i] > s[j]: # s[1] > s[0] : True -> dp=[1,1,1,1,1,1] -> dp=[1,2,1,1,1,1]
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))