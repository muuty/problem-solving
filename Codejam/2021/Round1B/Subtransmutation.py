import sys

def maximize(A,B, needs, metals):
    for i in range(0, len(metals)):
        if len(metals) -i - A >= 0:
            if len(metals) - i < len(needs):

                change =  metals[-i] - needs[len(metals) - i]
                if change > 0:
                    metals[-i - A] += change
                    if len(metals) - i - B >= 0:
                        metals[-i - B] += change
                    metals[-i] = needs[len(metals)-i]
            else:
                metals[-i-A] += metals[-i]
                if len(metals) - i - B >= 0:
                    metals[-i-B] += metals[-i]
                metals[-i] = 0


    return metals

def is_enough(metals, needs):
    for i in range(len(needs)):
        if needs[i] > metals[i]:
            return False
    return True

input = sys.stdin.readline
T = int(input())


for t in range(1, T + 1):
    n, A, B = list(map(int, input().split()))
    needs = list(map(int, input().split()))
    i=n
    while True:

        metals = [0] * i + [1]
        maximized_metals= maximize(A,B,needs,metals)

        if is_enough(maximized_metals, needs):
            answer = i+1
            break
        else:
            i += 1
            if i > 402:
                answer = "IMPOSSIBLE"
                break

    print("Case #" + str(t) + ":", answer)