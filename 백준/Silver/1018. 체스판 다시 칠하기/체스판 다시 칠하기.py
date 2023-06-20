N, M = map(int, input().split())
arr = []
count = []

for i in range(N):
    arr.append(input())

for a in range(N-7): # 8*8로 자르기 위해, -7을 해줌
    for b in range(M-7): 
        index1 = 0 # 흰색으로 시작
        index2 = 0 # 검은색으로 시작
        for i in range(a, a+8): # 시작 지점
            for j in range(b, b+8): # 시작 지점
                if (i + j) % 2 == 0: # 작수인 경우
                    if arr[i][j] != 'W': # W가 아니면, 즉 B이면
                        index1 += 1 # W로 칠하는 갯수
                    if arr[i][j] != 'B': # B가 아니면, 즉 W이면
                        index2 += 1 # B로 칠하는 갯수
                else: # 홀수인 경우
                    if arr[i][j] != 'B': # B가 아니면, 즉 W이면
                        index1 += 1 # W로 칠하는 갯수
                    if arr[i][j] != 'W': # W가 아니면, 즉 B이면
                        index2 += 1 # B로 칠하는 갯수
        count.append(min(index1, index2)) # 최솟값 index append
print(min(count))