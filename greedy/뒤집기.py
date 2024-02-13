n = input()
count = 0
# 규칙성을 찾아야한다.
# 0 과 1- > 길이 1
# 01-> 1번 길이 2
# 010->1번,길이 3
# 0101->2번 길이 4
# 01010->2반 길이 5
for i in range(len(n)-1):
    if n[i] != n[i+1]:
        count += 1
    print((count+1)/2)
