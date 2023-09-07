import sys
input = sys.stdin.readline

N, M = map(int, input().split())
word_dict = {}

for _ in range(N):
    word = input().rstrip()
    
    if len(word) < M: # 단어 길이가 M 미만일 경우
        continue
    else: # 단어 길이가 M 이상인 경우
        if word in word_dict: # 단어가 있는 경우
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            
word_dict = sorted(word_dict.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))
# x[0] = eksdj, x[1] = 빈도수
# -x[1] = 자주 나오는 단어 앞배치
# -len(x[0]) = 단어 길이 길수록 앞배치
# x[0] = 단어 사전 순 정렬
# sorted 사용시 다중 조건으로 정렬 가능
for i in word_dict:
    print(i[0])