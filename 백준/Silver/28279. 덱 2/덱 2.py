from collections import deque # deque: 앞과 뒤에서 데이터를 처리할 수 있는 양방향 자료형 
import sys
input = sys.stdin.readline

dq = deque()
N = int(input())

for _ in range(N):
    comand = list(map(int,input().split()))
    if comand[0] == 1: # 1 X: 정수 X를 덱의 앞에 넣는다
        dq.append(comand[1])
    elif comand[0] == 2: # 2 X: 정수 X를 덱의 뒤에 넣는다.
        dq.appendleft(comand[1])
    elif comand[0] == 3: # 3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        print(dq.pop() if dq else -1)
    elif comand[0] == 4: # 4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        print(dq.popleft() if dq else -1)
    elif comand[0] == 5: # 5: 덱에 들어있는 정수의 개수를 출력한다.
        print(len(dq))
    elif comand[0] == 6: # 6: 덱이 비어있으면 1, 아니면 0을 출력한다.
        print(0 if dq else 1)
    elif comand[0] == 7: # 7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        print(dq[-1] if dq else -1)
    else: # 8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        print(dq[0] if dq else -1)