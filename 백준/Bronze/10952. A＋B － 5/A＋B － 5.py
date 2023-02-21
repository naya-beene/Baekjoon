import sys
while 1: # while 참일때 계속 반복
   A, B = map(int, sys.stdin.readline().split())
   if A == 0 and B == 0: # 0 0을 입력 받으면 break문 실행
      break
   print(A + B)