N = int(input())
x_list = []
y_list = []
for i in range(N):
    x, y = map(int, input().split()) # x, y 값 입력
    x_list.append(x) # x 축 리스트 추가
    y_list.append(y) # y 축 리스트 추가

# x, y축 각각 최대값과 최솟값을 빼준 후 곱해준다.
print((max(x_list) - min(x_list)) * (max(y_list) - min(y_list)))
