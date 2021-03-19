def solution(triangle):
    dp = []
    height = len(triangle)
    for i in range(0, height):
        dp.append([0]* (i+1))
        for j in range(0, i+1):
            if i == 0:
                dp[0][0] = triangle[0][0]
                continue

            if j != 0 and j != i:
                dp[i][j] = max([dp[i-1][j], dp[i-1][j-1]]) + triangle[i][j] 
            elif j ==0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j] 

    return max(dp[height-1])


