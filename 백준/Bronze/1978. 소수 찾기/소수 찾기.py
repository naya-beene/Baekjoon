N = int(input())
Nlist = list(map(int, input().split()))
cnt = 0
for i in Nlist:
   for j in range(2, i+1): # 소수 이기 때문에 1을 제외한 2부터 시작
      if i % j == 0: 
         if i == j:  
            cnt += 1
         break
print(cnt)