import sys
N = int(sys.stdin.readline())
member = []

for i in range(N):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    member.append((age, name))

member.sort(key = lambda x : x[0]) # (age, name)에서 age만 비교
                                   # lambda 인자 : 표현식
for i in member:
    print(i[0], i[1])