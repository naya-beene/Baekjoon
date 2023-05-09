N, K = map(int, input().split())
Nlist = []
for i in range(1, N+1):
   if N % i ==0:     # 나머지가 0일때만 Nlist에 저장
      Nlist.append(i)

if len(Nlist) < K:   # N의 약수가 K보다 적어서 존재하지 않을경우
   print(0)
else:
   print(Nlist[K-1]) # 인덱스 번호에 맞게 [K-1] 째로 지정