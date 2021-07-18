
T = int(input())


def flip(s):
    if s == '1':
        return '0'
    else:
        return ''.join('1' if x == '0' else '0' for x in s).lstrip('0')

def not_count(s):
    s += '0'  # if s ends with '1', it requires one more "not" operation, which could be easily counted by appending a '0'
    return sum([int(s[i] != s[i-1]) for i in range(len(s)-1)])

def find_prefix_and_count(S, E):
    result = float("inf")
    X = 0
    #X는 Flip count 세기
    while S != "0":
        # S가 E와 앞부분이 같고, X >
        if S == E[:len(S)] and X >= not_count(E[len(S):]):
            return X+(len(E)-len(S)), None
        S = flip(S)
        X += 1
    return result, X

def double_or_noting(S,E):

    result, X = find_prefix_and_count(S, E)
    if result != float("inf"):
        return result
    if X >= not_count(E):
        return X+len(E)-(E[0] == '0')
    cnt = not_count(E[1:])
    if cnt == 0:
        return X+1+(len(E)-1)  # S =X=> "0" =1=> "1" =(len(E)-1)=> "10*"
    if cnt == 1:
        return X+1+len(E)+1  # S =X=> "0" =1=> "1" =k=> "100+" =1=> "11+" =(len(E)-k)=> "11+0*", where 2 <= k <= len(E)
    return "IMPOSSIBLE"

print(flip("111000101"))

for t in range(T):
    S, E = input().split()
    answer = double_or_noting(S, E)
    print("Case #", t+1, ": ", answer)