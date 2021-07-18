N, M, L = list(map(int, input().split()))
locations = sorted(list(map(int, input().split())))

left = 1
right = L
answer = 0
locations = [0] + locations + [L]

while left <= right:
    mid = (left + right) // 2
    count = 0
    more_than = False
    for i in range(1, len(locations)):
        count += (locations[i] - locations[i-1] - 1) // mid
        #print(i, ": ", locations[i] - locations[i-1], (locations[i] - locations[i-1]) // mid)
        if count > M:
        #    print("exeed")
            more_than = True
            break


    if more_than:
        left = mid+1
    else:
        answer = mid
        right = mid-1

print(answer)


