word = input().upper()
word_list = list(set(word)) # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for i in word_list:
    cnt = word.count(i)
    cnt_list.append(cnt) # count 숫자를 리스트에 추가
    
if cnt_list.count(max(cnt_list)) > 1: # count 숫자 최대값이 중복되면 출력
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list)) # count 숫자 최대값 인덱스(위치)
    print(word_list[max_index])