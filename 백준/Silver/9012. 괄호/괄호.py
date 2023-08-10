import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    stack = []
    PS = input()
    for i in PS:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else: # 스택에 괄호가 없을 경우 NO출력
                print('NO')
                break
    else: # break문으로 끊기지 않고 수행됐을 경우 수행
        if not stack: # break 문으로 안끊기고 스택이 비어있다면 PSV 충족
            print("YES")
        else: # break가 걸렸더라도 스택에 괄호가 있다면 NO
            print('NO')