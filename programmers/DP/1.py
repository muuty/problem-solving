def solution(N, number):

    dp = {}

    all_digit_number = N

    for i in range(1,9):
        dp[i] = []
        for j in range(1,(i)//2 + 1):
            dp[i] += [v1 + v2 for v1 in dp[i-j] for v2 in dp[j]]
            dp[i] += [v1 * v2 for v1 in dp[i-j] for v2 in dp[j]]
        
        for j in range(1, i):
            dp[i] += [v1 // v2 for v1 in dp[i-j] for v2 in dp[j] if v2 != 0]
            dp[i] += [v1 - v2 for v1 in dp[i-j] for v2 in dp[j]]

        dp[i].append(all_digit_number)



        dp[i] = list(set(dp[i]))
        all_digit_number = all_digit_number * 10 + N
        if number in dp[i]:
            return i

    return -1
