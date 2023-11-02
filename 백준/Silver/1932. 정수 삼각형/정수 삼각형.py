import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    
# dp[i]의 양 끝을 제외하고는 dp[i-1][j-1] 와 dp[i-1][j] 를 비교하여 최댓값을 더한다.    
for i in range(1, n):
    for j in range(i + 1):
        if j == 0: 
            arr[i][j] += arr[i-1][j] # dp[i]의 j==0인 경우 -> dp[i][j] += dp[i-1] 
        elif j == i:
            arr[i][j] += arr[i-1][j-1] # dp[i]의 j==맨 끝의 경우 -> dp[i][j] += dp[i-1][j-1]
        else: # 두개의 값중 최댓값
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
            
print(max(arr[n-1]))
