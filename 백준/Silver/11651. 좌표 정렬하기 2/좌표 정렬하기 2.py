import sys

N = int(input())
arr = []
for i in range(N): # arr리스트에 [x, y]를 추가 [[3, 4], [1, 1], [2, 2], ...] 형식
    [x, y] = map(int, sys.stdin.readline().split())
    arr.append([y, x]) # x, y 좌표를 뒤집어서 추가

arr = sorted(arr) # sorted함수로 오름차순 정렬

for i in range(N): # 정렬된 arr에 들어있는 리스트 출력
    print(arr[i][1], arr[i][0]) # 이중구조 리스트 인덱싱
    # [y, x] 형태가 저장되어있기 때문에 x, y형태로 출력
    