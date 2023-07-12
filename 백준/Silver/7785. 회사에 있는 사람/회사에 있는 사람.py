import sys
input = sys.stdin.readline
N= int(input())
temp = dict() # 딕셔너리 형

for _ in range(N):
    name, log = map(str, input().split())
    
    # 출입을 했다면 딕셔너리로 받기
    if log == "enter":
        temp[name] = log
    # 퇴근을 했다면 삭제
    else:
        del temp[name]
    
# 딕셔너리 순의 역순으로 정렬
temp = sorted(temp.keys(), reverse=True)

for i in temp:
    print(i)