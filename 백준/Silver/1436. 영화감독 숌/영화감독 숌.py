N = int(input())
cnt = 0
num = 666

while True:
    if '666' in str(num): # N번째 수에 '666'이 포함되어있을때
        cnt += 1 # cnt + 1
    if cnt == N: # cnt와 N번째 수가 같다면
        print(num) # num 출력하고
        break # while문 종료
    num += 1 # 666이 포함된 수가 나올 때 까지 num 1씩 증가시킴