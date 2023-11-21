import sys
input = sys.stdin.readline

N = int(input()) # 포도주 잔의 개수

data = [0] * 10001
for i in range(1, N + 1):
    data[i] = int(input()) # 포도주의 양

dp = [0] * 10001 # 최대 포도주 양을 저장할 list
dp[1] = data[1]  # 1번째 값은 첫번째 포도주의 양
dp[2] = data[1] + data[2] # 2번째 값은 첫번째, 두번째 포도주 양의 합

for i in range(3, N + 1): # 3번째부터 반복
    # 현재 포도주를 마시지 않았을 경우, 현재 포도주와 이전 포도주를 마셨을 경우, 마시지 않았을 경우를 비교
    dp[i] = max(dp[i - 1], data[i] + data[i - 1] + dp[i - 3], data[i] + dp[i - 2])

print(max(dp)) # 구한 dp 중 최댓값 출력