M = int(input())
N = int(input())

sosu_list = []
for i in range(M, N+1):
    cnt = 0
    if i > 1 :
       for j in range(2, i): # 2부터 i-1까지
           if i % j == 0:
              cnt += 1
              break # 2부터 i-1까지 나눈 몫이 0이면 cnt 증가 이후 break
       if cnt == 0:
          sosu_list.append(i) # 소수 이면 리스트에 추가

if len(sosu_list) > 0:
   print(sum(sosu_list))
   print(min(sosu_list))
else:
   print(-1)