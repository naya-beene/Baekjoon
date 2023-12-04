import sys
input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()
l1, l2 = len(word1), len(word2)
dp = [0] * l2

for i in range(l1):
    cnt = 0 # 누적변수 선언
    for j in range(l2):
        if cnt < dp[j]:
            cnt = dp[j]
        elif word1[i] == word2[j]:
            dp[j] = cnt + 1 # 글자가 같을 경우 누적변수 + 1
print(max(dp))