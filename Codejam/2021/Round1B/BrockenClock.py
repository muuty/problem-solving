T = int(input())
circle = 360 * 12 * 10 ** 10
indexes = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2,0], [2, 0, 1], [2, 1, 0]]

HOUR = 3600 * (10**9)
MIN = 60 * (10 ** 9)
SECOND = 10 ** 9

def get_hmsn(thetas):
    for index in indexes:
        a_h, a_m, a_s = [thetas[i] for i in index]
        for h in range(0, 12):
            for m in range(0, 60):
                t1 = (a_s - a_h + (60 * h + m) * circle)
                t2 = (a_m - a_h + h * circle)
                print()
                if t1 % 719 == 0 and t2 % 11 == 0 and t1 // 719 == t2 // 11:
                    T = t1 // 719
                    H = T // HOUR
                    M = (T % HOUR) // MIN
                    S = ((T % HOUR) % MIN) // SECOND
                    N = T % HOUR % MIN % SECOND
                    return [H, M, S, N]


for t in range(1, T+1):
    thetas = list(map(int, input().split()))
    h,m,s,n = get_hmsn(thetas)

    print("Case #" + str(t) + ":" , h,m,s,n)