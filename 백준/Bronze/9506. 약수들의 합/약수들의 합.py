while True:
   n = int(input())
   nlist = []
   if n == -1:
      break
   for i in range(1, n):  
      if n % i == 0:       # 약수일 경우 저장
         nlist.append(i)
   if sum(nlist) == n:     # 완전수 일 경우 출력
         print(n, " = ", " + ".join(str(i) for i in nlist), sep="")
   else:
      print(n, "is NOT perfect.")