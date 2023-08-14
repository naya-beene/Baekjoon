import sys
input = sys.stdin.readline

stack = []
N = int(input()) # 학생들 수
number = list(map(int, input().split())) # 학생들 번호표
target = 1 # 간식 받을 사람 번호

while number: #학생들 번호표가 존재할때 반복
    if number[0] == target: # 번호표가 target 값과 일치하면 pop 이후 target + 1 
        number.pop(0)
        target += 1
    else: # 첫번째 번호표와 target 값이 같지 않다면 stack 리스트에 그 값을 추가하며 pop
        stack.append(number.pop(0))
    
    while stack: #stack이 존재할때 반복
        if stack[-1] == target: # stack의 마지막값이 target 이면 그 값을 pop시키고 target + 1
            stack.pop()
            target += 1
        else:
            break

print("Nice" if not stack else "Sad")