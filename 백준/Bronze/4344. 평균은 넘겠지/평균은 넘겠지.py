import sys
C = int(input())

for i in range(C):
    Score = list(map(int, input().split()))
    Mean = sum(Score[1:])/Score[0]
    cnt = 0
    for j in range(1, len(Score)):
        if Score[j] > Mean:
            cnt += 1
    percent = 100*cnt/Score[0]
    print("{:.3f}%".format(round(percent,3)))