import sys
N_list = []
for _ in range(9):
    N = int(sys.stdin.readline())
    N_list.append(N)
print(max(N_list))
print(N_list.index(max(N_list))+1)