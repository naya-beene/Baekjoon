A, X = map(int, input().split()) 
A_list = list(map(int, input().split()))
for i in range(A):
    if A_list[i] < X: #크기비교후 X보다 작을때 출력
       print(A_list[i], end=" ")