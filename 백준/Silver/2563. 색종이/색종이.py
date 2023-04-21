N = int(input()) # 종이 갯수 입력
array = [[0 for _ in range(101)] for _ in range(101)] # 2차원 배열 선언

for _ in range(N): 
    x, y = map(int, input().split()) # 종이 위치 입력
    for row in range(x, x + 10): # 가로, 세로 크기가 10인 정사각형 이기때문에 10씩 더해줌
        for col in range(y, y + 10):
            array[row][col] = 1 # 색종이 붙힌 위치를 1로 지정
result = 0
for i in array:
    result += i.count(1) # 1을 카운트후 결과값에 더해줌
print(result)