def get_duration(index, prices):
    price = prices[index]
    for i in range(index + 1, len(prices)):
        if prices[i] < price:
            return i  - index
    return len(prices) - 1 - index
def solution(prices):

    answer = [get_duration(i, prices) for i in range(len(prices))]
    return answer


print(solution([1,2,3,2,3]))