#  팩토리얼
# n!=1*2*3...*(n-1)*n

# 반복저으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= 1
    return result


# 재귀적 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    # n!=(n-1)*n 그대로 구현
    return n*factorial_recursive(n-1)
