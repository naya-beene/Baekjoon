import sys
input = sys.stdin.readline

stack = []
N = int(input())

for _ in range(N):
    command = input().split()
    
    if command[0] == '1': # 1: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
        stack.append(command[1])
    elif command[0] == '2': # 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == '3': # 3: 스택에 들어있는 정수의 개수를 출력한다.
        print(len(stack))
    elif command[0] == '4': # 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == '5': # 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
        if stack:
            print(stack[-1])
        else:
            print(-1)
        