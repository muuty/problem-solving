import sys
readline = sys.stdin.readline

T = int(input())

for t in range(T):
    cost = 0
    N = int(input())
    numbers = list(map(int, readline().split()))

    for i in range(len(numbers)-1):
        j = numbers[i:].index(min(numbers[i:])) + i
        numbers[i:j+1] = numbers[i:j+1][::-1]
        cost += j - i + 1
    print("Case #" + str(t+1) + ": ", cost)