from collections import deque # deque: 앞과 뒤에서 데이터를 처리할 수 있는 양방향 자료형
import sys
input = sys.stdin.readline

N = int(input())
dq = deque([])

for _ in range(N):
    comand = input().split()
    if comand[0] == 'push': # push X: 정수 X를 큐에 넣는 연산이다
        dq.append(comand[1])
    elif comand[0] == 'pop': # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다.
        if len(dq):          # 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
            print(dq.popleft())
        else:  
            print(-1)
    elif comand[0] == 'size': # size: 큐에 들어있는 정수의 개수를 출력한다.
        print(len(dq))
    elif comand[0] == 'empty': # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
        if len(dq):
            print(0)
        else:
            print(1)
    elif comand[0] == 'front': # front: 큐의 가장 앞에 있는 정수를 출력한다.
        if len(dq):            # 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
            print(dq[0])
        else:
            print(-1)
    elif comand[0] == 'back': # back: 큐의 가장 뒤에 있는 정수를 출력한다.
        if len(dq):           # 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
            print(dq[-1])
        else:
            print(-1)