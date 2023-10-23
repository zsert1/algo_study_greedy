n=int(input())
data=list(map(int,input().split()))
target=1

data.sort()
for x in data:
    if target<x:
        break
    target+=x
print(target)