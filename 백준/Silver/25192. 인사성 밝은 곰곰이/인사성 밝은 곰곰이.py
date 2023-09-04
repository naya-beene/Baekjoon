import sys
input = sys.stdin.readline

N = int(input())
s = set()
cnt = 0
input()

for _ in range(N - 1):
    user = input().strip()
    if user == "ENTER":
        cnt += len(s)
        s.clear()
    else:
        s.add(user)
cnt += len(s)

print(cnt)