chess = [1,1,2,2,2,8] #정해진 말의 수
pice = list(map(int, input().split()))

for i in range(6):
    print(chess[i] - pice[i], end = ' ')