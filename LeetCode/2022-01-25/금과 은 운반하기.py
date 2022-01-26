def solution(a, b, golds, silvers, weights, times):
    left = 0
    right = (2*((a+b) // min(weights) + 1) + 1) * max(times)
    while left < right:
        mid = (left + right)//2
        moves = [mid // time for time in times]
        delivers = [(move+1) // 2 for move in moves]
        max_deliver_amounts = [delivers[i] * weights[i] for i in range(len(weights))]
        if sum(max_deliver_amounts) < a+b:
            left = mid + 1
            continue

        gold_amount = 0
        silver_amount = 0
        free_amount = 0
        for i in range(len(weights)):
            if golds[i] + silvers[i] < max_deliver_amounts[i]:
                # 금, 은 다 가져갈 수 있으면 그냥 다 가져가면 됨
                gold_amount += golds[i]
                silver_amount += silvers[i]
            else:
                min_x = max([max_deliver_amounts[i] - silvers[i], 0])
                min_y = max([max_deliver_amounts[i] - golds[i], 0])
                gold_amount += min_x
                silver_amount += min_y
                free_amount += min([max_deliver_amounts[i], silvers[i]]) - min_y
        if max([a - gold_amount, 0]) + max([b - silver_amount, 0]) <= free_amount:
            # can deliver
            right = mid
            continue
        else:
            left = mid + 1
            continue

    return left


print(solution(10,10,[100],[100],[7],[10]))
print(solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1]))
print(solution(100,10,[6,4],[4,6],[2,2],[10,1]))
