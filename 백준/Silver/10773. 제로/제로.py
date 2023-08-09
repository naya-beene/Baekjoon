import sys
input = sys.stdin.readline

jangbu = []
K = int(input())

for _ in range(K): 
    N = int(input())
    if not N == 0: # 정수 N이 0이 아니면 장부에 추가
        jangbu.append(N)
    else: # 정수 N이 0이면 장부에서 제거
        jangbu.pop()
print(sum(jangbu)) # 장부합