import sys

N = int(sys.stdin.readline())
word = []

for i in range(N):
    word.append(sys.stdin.readline().strip())
set_word = set(word) # 중복제거
word = list(set_word) # 다시 리스트형식으로 변경
word.sort()  # 괄호 안에 아무 값도 넣지 않으면 알파벳 순서대로 정렬
word.sort(key = len) # 문자열 길이 순으로 정렬

for i in word:
    print(i)