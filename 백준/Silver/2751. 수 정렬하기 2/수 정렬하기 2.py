import sys

N = int(input()) # 개수 입력받기
arr = [] 
for i in range(N): # 개수 만큼 반복하며
    arr.append(int(sys.stdin.readline())) #리스트로 받기
    
arr.sort() # 오름차순 정렬

for j in arr: # 한 줄씩 출력
    print(j)

# input(), sys.stdin.readline() 차이점
# input() 내장 함수는 sys.stdin.readline()과 비교해서 prompt message를 출력하고,
# 개행 문자를 삭제한 값을 리턴하기 때문에 느리다.