
def add_new_min_cost(connected, costs, total_cost):
    for cost in costs:
        if connected[cost[0]] + connected[cost[1]] == 0:
            total_cost = add_cost(connected, cost, total_cost)
            break
    return total_cost

def add_cost(connected, cost, total_cost):
    connected[cost[0]] = 1
    connected[cost[1]] = 1
    total_cost += cost[2]
    return total_cost

def solution(n, costs):
    nodes = [i for i in range(n)]

    costs.sort(key = lambda x: x[2])
    total_cost = 0
    connected = {i : 0 for i in nodes}
    total_cost = add_new_min_cost(connected, costs, total_cost)
    for _ in range(0,n-1):
        no_more_edge = True
        for cost in costs:
            node1, node2, cost_value = cost
            if connected[node1] + connected[node2] == 1:
                total_cost = add_cost(connected, cost, total_cost)
                no_more_edge = False
                break
        if no_more_edge:
            total_cost = add_new_min_cost(connected, costs, total_cost)

    return total_cost

if __name__ == '__main__':
    print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
    #print(solution("4177252841", 8))
