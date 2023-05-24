x_list = []
y_list = []
for i in range(3): # 각각의 세점 입력
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
    
for i in range(3): # 직사각형 이기에 count개수가 1인 것을 출력
    if x_list.count(x_list[i]) == 1:
        x = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y = y_list[i]
print(x, y)
    