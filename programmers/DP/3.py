
def is_puddle(i,j, puddles):
    for puddle in puddles:
        if puddle[0] == j and puddle[1] == i:
            return True
    return False

def solution(m, n, puddles):
    mod = 1000000007
    dp= [[0] * (m+1) for _ in range(0,n+1)]
    dp[1][1] = 1
    for i in range(3, m+n+2):
        for j in range(0, i):
            if i-j<=n and j<=m:
                if is_puddle(i-j, j, puddles):
                    dp[i-j][j] = 0
                else:
                    dp[i-j][j] = dp[i-j][j-1] + dp[i-j-1][j] % mod
    
    return dp[n][m]  % mod


#print(solution(2, 2, []), 2)
#print(solution(3, 3, []), 6)
#print(solution(3, 3, [[2, 2]]), 2)
#print(solution(3, 3, [[2, 3]]), 3)
#print(solution(3, 3, [[1, 3]]), 5)
#print(solution(3, 3, [[1, 3], [3, 1]]), 4)
#print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
#print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0) 
#print(solution(4, 4, [[3, 2], [2, 4]]), 7)
#print(solution(100, 100, []), 690285631)
