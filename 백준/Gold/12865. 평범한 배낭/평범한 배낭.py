import sys
input = sys.stdin.readline
# 냅색 알고리즘 해당문제는 물건을 나눌 수 없을 때의  0-1 배낭문제(0-1Knapsack Problem)
N, K = map(int, input().split()) # N = 물품의 수, K = 버틸 수 있는 무게
dp = [[0,0]]
knapsack = [[0 for _ in range(K +1)] for _ in range(N + 1)] # x, y축 각각 K까지의 무게 N개 개수 만큼의 배열 생성

for i in range(N):
    dp.append(list(map(int, input().split())))
    
#냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = dp[i][0]
        value = dp[i][1]
        
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] # weight 보다 작으면 위 값을 그대로 가져옴
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])
        #   knapsack[i][j] = max(현재 물건 가치 + knapsack[이전 물건][현재 가방 무게 - 현재 물건 무게], knapsack[이전 물건][현재 가방 무게])
print(knapsack[N][K])