arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42) # 입력받은 값을 42로 나눈 나머지 저장
arr = set(arr) # set을 이용한 집합 자료형생성 / 중복제거 
print(len(arr)) # 개수 출력
