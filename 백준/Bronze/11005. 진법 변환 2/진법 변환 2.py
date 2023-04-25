N, B = map(int, input().split())
result = ''
tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" # 10진법이면 9까지, 36WLSQJQDLAUS Z까지 표현

while N != 0: # N을 B로 나눈 나머지를 마지막칸에 채움
    result += str(tmp[N % B]) # 위치로 진법 변환
    N //= B  # N을 B로 나눈 몫이 N이 됨

print(result[::-1])