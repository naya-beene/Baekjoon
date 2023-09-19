import sys
input = sys.stdin.readline

N = int(input())

def hanoi(N, A, B, C): # N: 원판 개수/ A: 시작하는 장대번호/ B: 옮기려는 장대 번호/ C: 나머지 남은 장대번호
    if N == 0: return # base case 원판이 0개 남으면 그대로 return
    hanoi(N-1, A, C, B)
    print(A, B)
    hanoi(N-1, C, B, A) # 하노이탑 최소 이동 횟수
    
print(2**N-1)
hanoi(N, 1, 3, 2)