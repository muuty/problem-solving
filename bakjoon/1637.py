

N = int(input())

def get_count_until_x(x, acb):
    sum = 0
    for i in range(N):
        a, c, b = acb[i]
        sum += max(0, (min(c, x) - a) // b + 1)


    return sum


acb = []
for i in range(N):
    acb.append(list(map(int, input().split())))

left = 1
right = 2147483647
answer = None
while left <= right:
    mid = (left + right)//2
    sum =  get_count_until_x(mid, acb)
    if sum % 2 == 0:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

if answer == None:
    print("NOTHING")
else:
    print(answer, get_count_until_x(answer, acb) - get_count_until_x(answer-1, acb))