# 작은 두 변의 길이의 합이 제일 긴 변의 길이보다 커야 된다는 점을 사용하면 쉽게 풀 수 있다.
li = sorted(list(map(int, input().split())))
tri = li[0] + li[1] +min(li[2], li[0]+li[1]-1)
print(tri)