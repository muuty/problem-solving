import sys
readline = sys.stdin.readline

T = int(input())

for t in range(T):
    X, Y, art = list(readline().split())
    X = int(X)
    Y = int(Y)
    art = list(art)
    cost = 0

    q_count = 0
    q_start = 0
    q_prev = 0
    q_next = 0

    for i in range(len(art)):
        if i != 0 and art[i] != '?':
            if art[i-1] == '?':
                if art[i] == 'C' and q_prev == 'J':
                    cost += Y
                elif art[i] == 'J' and q_prev == 'C':
                    cost += X
                q_count = 0

            elif art[i-1] == 'C' and art[i] == 'J':
                cost += X
            elif art[i-1] == 'J' and art[i] == 'C':
                cost += Y

        elif art[i] == '?':
            if q_count == 0:
                q_count += 1
                if i > 0:
                    q_prev = art[i-1]

    print("Case #" + str(t+1) + ": ", cost)
