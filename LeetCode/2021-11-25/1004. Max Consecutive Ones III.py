def longestOnes(self, A, K):
    i = 0
    for j in xrange(len(A)):
        K -= 1 - A[j]
        if K < 0:
            K += 1 - A[i]
            i += 1
    return j - i + 1