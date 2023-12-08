import sys
input = sys.stdin.readline

N, K = map(int, input().split())
N_list = list(map(int, input().split()))

prefix_sum = sum(N_list[:K]) # sum() 을 이용하여  N_list[0]번 부터 N_list[K]에 해당하는 값을 더함
prs_list = [prefix_sum] # prefix_sum 값을 리스트 형식으로 저장

for i in range(N-K):
    prefix_sum = prefix_sum - N_list[i] + N_list[i+K]
    prs_list.append(prefix_sum)

print(max(prs_list))