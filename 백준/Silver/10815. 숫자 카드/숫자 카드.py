import sys
N = int(sys.stdin.readline())
card_num = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_num = list(map(int, sys.stdin.readline().split()))

dict = {}
for i in range(len(card_num)):
    dict[card_num[i]] = 0
    
for j in range(M):
    if M_num[j] not in dict:
        print(0, end = ' ')
    else:
        print(1, end = ' ')