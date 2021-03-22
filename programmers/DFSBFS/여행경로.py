def solution(tickets):
    tickets.sort(reverse=True)
    print(tickets)
    routes = {}
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
            
    answer = []
    stack = ['ICN']
    
    while stack:
        print("stack : ",stack)
        print("answer : ", answer)
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(routes[top].pop())
    
    return answer.reverse()

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])