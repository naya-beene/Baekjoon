import sys
s = sys.stdin.readlines()
for i in s:
    print(i.rstrip()) 
# readlines()로 문자열을 받아오면 개행문자 '\n' 도 같이 받기 때문에 rstrip()함수를 사용해준다.