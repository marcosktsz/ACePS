T = int(input())

for _ in range(T):
    _ = int(input())
    S = list(map(int, input().split()))

    bucket = []
    res = [0 for _ in S]
    for i in range(len(S) - 1, -1, -1):
        if not bucket or S[i] < bucket[-1]:
            bucket.append(S[i])
            res[i] = len(bucket)
        else:
            for j in range(len(bucket)):
                if S[i] > bucket[j]:
                    bucket[j] = S[i]
                    res[i] = j + 1
                    break

    bucket = []
    res2 = [0 for _ in S]
    for i in range(len(S)):
        if not bucket or S[i] > bucket[-1]:
            bucket.append(S[i])
            res2[i] = len(bucket)
        else:
            for j in range(len(bucket)):
                if S[i] < bucket[j]:
                    bucket[j] = S[i]
                    res2[i] = j + 1
                    break

    print(" ".join(str(res[i] + res2[i] - 1) for i in range(len(S))))
