N, M = map(int, input().split()) #행렬 크키 입력
A, B = [], [] #행렬 받을 리스트 선언

# A, B 에 각각 행렬 입력 받기
for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)
    
# 행렬 A, B 를 더한 행렬 출력
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()