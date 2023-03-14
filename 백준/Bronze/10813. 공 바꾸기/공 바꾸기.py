import sys
N, M = map(int, sys.stdin.readline().split())
basket = [i for i in range(1, N+1)] #1번부터 N번 바구니가 있는 공의 번호 저장 리스트 변수

for _ in range(M): # M번 교환 반복문
    i, j = map(int, sys.stdin.readline().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
print(*basket)