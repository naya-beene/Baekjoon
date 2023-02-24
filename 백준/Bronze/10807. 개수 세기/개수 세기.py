N = int(input()) 
N_list = list(map(int, input().split())) #리스트 입력받기
v = int(input()) 
print(N_list.count(v)) # 리스트 특정 엘리먼트의 반복 횟수를 세는 count 함수 