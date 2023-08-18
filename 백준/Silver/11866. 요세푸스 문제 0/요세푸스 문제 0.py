from collections import deque # deque: 앞과 뒤에서 데이터를 처리할 수 있는 양방향 자료형 
import sys

input = sys.stdin.readline
dq = deque()
result = []

N, K = map(int, input().split()) 

for i in range(1, N+1):
    dq.append(i)

while dq:
    for i in range(K-1):
        dq.append(dq.popleft()) # popleft() = 제일 앞의 요소 삭제
    result.append(dq.popleft())
    
print("<", end='')
print(', '.join(map(str, result)), end='')
print(">")
