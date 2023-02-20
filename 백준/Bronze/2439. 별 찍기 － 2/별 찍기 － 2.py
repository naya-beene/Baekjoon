N = int(input())
for i in range(1,N+1):
   print(('*' * i).rjust(N)) #오른쪽 정렬 = rjust(전체자리수, 공백이 있으면 공백을 채울 텍스트) / 왼쪽 정렬 = ljust()
