import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dict = {}

for i in range(1, N+1):
    poketmon_name = input().rstrip()
    dict[i] = poketmon_name
    dict[poketmon_name] = i

for _ in range(M):
    quest = input().rstrip()
    if quest.isdigit(): # isdigit() : 문자열이 '숫자'로만 이루어져있는지 확인 하는 함수 False / True반환
        print(dict[int(quest)])
    else:
        print(dict[quest])