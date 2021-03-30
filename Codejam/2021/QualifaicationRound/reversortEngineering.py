import sys
readline = sys.stdin.readline


T = int(input())

for t in range(T):
    N, C = list(map(int, readline().split()))
    if C < N-1:
        answer = 'IMPOSSIBLE'
    elif C > (N-1)*(N+2)/2:
        answer = 'IMPOSSIBLE'
    else:
        C = C - N + 1
        answer = [1] * (N-1)
        for i in range(N-1):
            if C >= N - 1 - i:
                answer[i] = N-i
                C -= N - 1 -i
            else:
                answer[i] += C
                C = 0


        #reconstruct
        numbers = [0] * N
        index = [i+1 for i in range(0, N)]
        index_key = set([i+1 for i in range(0, N)])
        #print("answer : ", answer)
        for i in range(0,N-1):
            #print(i , "th iteration")


            numbers[index[i + answer[i] - 1] - 1] = i + 1
            index[i:answer[i]+i ] = index[i:answer[i]+i][::-1]
            #print("index : ", index)
            #print("numbers : ", numbers)


        numbers[numbers.index(0)] = N
        answer = numbers

    if answer == 'IMPOSSIBLE':
        print("Case #" + str(t+1) + ": ", answer)
    else:
        print("Case #" + str(t+1) + ": ", *answer)
