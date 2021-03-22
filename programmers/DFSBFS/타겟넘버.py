count = 0
Numbers = 0
Target = 0


def dfs(value, index):
    global count 
    if index == len(Numbers) and value == Target:
        count = count+ 1
    if index < len(Numbers):
        dfs(value + Numbers[index], index+1)
        dfs(value - Numbers[index], index+1)



def solution(numbers, target):

    global Numbers
    global Target
    
    Numbers = numbers
    Target = target
    print(Numbers )
    dfs(0, 0)
    
    return count


print(solution([1,1,1,1,1], 3))