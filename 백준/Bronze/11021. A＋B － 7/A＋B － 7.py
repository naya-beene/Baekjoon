import sys
T = int(input()) #Test case 입력
for i in range(1,T+1): # 1부터 T까지를 i 에 저장
   A, B = map(int, sys.stdin.readline().split()) # 반복되는 값을 받기 위해 sys.stdin.readline 사용
   print(f'Case #{i}: {A+B}') # f-string을 이용 {} 안에 변수값을 넣음