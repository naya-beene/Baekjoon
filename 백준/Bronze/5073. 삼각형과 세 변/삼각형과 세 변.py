while True:
    li = sorted(list(map(int, input().split()))) # 정렬한 새로운 리스트를 반환
    if li[0] == li[1] == li[2] == 0:
        break
    if li[0] + li[1] <= li[2]:
        print('Invalid')
    elif li[0] == li[1] == li[2]:
        print('Equilateral')
    elif li[0] == li[1] or li[0] == li[2] or li[1] == li[2]:
        print('Isosceles')
    else:
        print('Scalene')
