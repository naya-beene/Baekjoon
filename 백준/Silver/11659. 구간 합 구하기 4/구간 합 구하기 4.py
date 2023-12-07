import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
prefix_sum = [0] # Prefix sum(구간 합)
sum = 0

for i in range(N): # 시간 복잡도를 줄이기 위해 구간합을 미리 구해놓음
    sum += N_list[i]
    prefix_sum.append(sum)
    
for i in range(M):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])

# M개의 데이터와 N개의 입력이 있을 때, 전체 구간 합을 구하는 시간 복잡도는 O(M + N)이됨