import sys
input = sys.stdin.readline

N = int(input())
rgb = []

for _ in range(N):
    rgb.append(list(map(int, input().split())))

for i in range(1, N): # 1부터 시작하는 이유 다음 입력값이 이전 입력값의 최소값을 사용하기 때문
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]
    
print(min(rgb[N-1]))