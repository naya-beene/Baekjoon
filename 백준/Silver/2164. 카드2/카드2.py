from collections import deque # deque: 앞과 뒤에서 데이터를 처리할 수 있는 양방향 자료형
import sys
input = sys.stdin.readline

N = int(input()) 
dq = deque()

for i in range(N): # N개의 카드 넣기
    dq.append(i + 1)
    
while len(dq) > 1: 
    dq.popleft()    # 제일 위에 있는 카드 버리기
    dq.append(dq.popleft()) # 그 다음 제일 위에 있는 카드를 제일 아래에 있는 카드로 옮기기

print(dq.pop())