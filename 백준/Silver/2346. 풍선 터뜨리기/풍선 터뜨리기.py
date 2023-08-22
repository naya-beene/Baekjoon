import sys
from collections import deque 
input = sys.stdin.readline

N = int(input())
dq = deque(enumerate(map(int, input().split()))) 
result = []

while dq:
    idx, pop_num = dq.popleft()
    result.append(idx + 1)
    
    if pop_num > 0:
        dq.rotate(-(pop_num - 1))
    elif pop_num < 0:
        dq.rotate(-pop_num)

print(' '.join(map(str, result)))

# enumerate: 주어진 입력을 컬렉션 또는 튜플로 가져와 열거(Enumerate) 객체로 반환
# pop을 하더라도 초기 인덱스 정보는 끝까지 유지되어야 하기때문에 enumerate 사용
# enumerate 사용 전
# deque([3, 2, 1, -3, -1])
# enumerate 사용 후
# deque([(0, 3), (1, 2), (2, 1), (3, -3), (4, -1)])

# deque.rotate(): rotate(-1)은 원형 큐를 반시계방향으로 1칸 회전시키고, rotate(1)은 시계방향으로 1칸 회전시킨다고 생각하면 쉽다.