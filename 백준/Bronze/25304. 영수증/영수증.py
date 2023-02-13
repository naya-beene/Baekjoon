X = int(input()) # 영수증에 적힌 총 금액
n = int(input()) # 구매한 물건의 종류의 수
sum = 0 # 구매한 가격과 개수로 계산한 총 금액
for _ in range(n):
   a, b = map(int, input().split()) # a 구매한가격, b 개수 입력
   sum += a * b # 구매한 가격 개수만큼 곱한뒤 sum에 더해줌
   
if sum == X:
   print('Yes')
else:
   print('No')