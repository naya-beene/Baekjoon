import sys
T = int(input()) # Test case
for _ in range(T):
   a, b = map(int, sys.stdin.readline().split())  #반복문으로 여러줄을 입력 받을 땐 sys.stdin.readline() 을 사용해야 시간초과가 발생하지 않는다.
   print(a+b)