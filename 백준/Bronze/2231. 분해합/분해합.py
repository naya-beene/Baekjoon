N = int(input())

for i in range(1, N+1): # 분해합의 생성자 찾기
    num = sum((map(int, str(i)))) # i의 각 자릿수를 더함
    num_sum = i + num # 분해합 = 생성자 + 각 자릿수의 합
    # 처음으로 분해합과 입력값이 같을때가 가장 작은 생성자를 가짐
    if num_sum == N: 
        print(i)
        break
    if i == N: # 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻
        print(0)