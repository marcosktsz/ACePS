T = int(input())

for _ in range(T):
    _ = int(input())
    S = list(map(int, input().split()))

    sub = {i: [i] for i in S}
    maxSub = {i: 1 for i in S}

    poldo = [1 for _ in S]

    for i, el_i in enumerate(reversed(S)):
        index = len(S) - 1 - i
        for j, el_j in enumerate(reversed(S[index:])):
            index_j = len(S) - 1 - j
            # if el_i < el_j and poldo[index] <= poldo[index_j]:
            if el_i < el_j and maxSub[el_i] <= maxSub[el_j]:
                sub[el_i] += sub[el_j]
                maxSub[el_i] = len(sub[el_i])
                if maxSub[el_j] < maxSub[el_i]:
                    for i in sub[el_j]:
                        maxSub[i] = maxSub[el_i]
            #     poldo[index] = poldo[index_j] + 1
            #     maxSub[el_i] += 1
    print(sub)
    # for i in maxSub.values():
    #     print(i, end=" ")

    # for ins_idx, ins in enumerate(S):
    #     prev = S[:ins_idx]
    #     next = S[ins_idx:]
    #     poldoPrev = [0] * len(prev)
    #     poldoNext = [0] * len(next)
    #
    #     for i, el_i in enumerate(reversed(prev)):
    #         index = len(prev) - 1 - i
    #         if el_i < ins:
    #             poldoPrev[index] += 1
    #             for j, el_j in enumerate(reversed(prev[index:])):
    #                 index_j = len(prev) - 1 - j
    #                 if el_j < ins:
    #                     if el_i < el_j and poldoPrev[index] <= poldoPrev[index_j]:
    #                         poldoPrev[index] = poldoPrev[index_j] + 1
    #
    #     for i, el_i in enumerate(reversed(next)):
    #         index = len(next) - 1 - i
    #         if el_i > ins:
    #             poldoNext[index] += 1
    #             for j, el_j in enumerate(reversed(next[index:])):
    #                 index_j = len(next) - 1 - j
    #                 if el_j > ins:
    #                     if el_i < el_j and poldoNext[index] <= poldoNext[index_j]:
    #                         poldoNext[index] = poldoNext[index_j] + 1
    #     print(max(poldoNext, default=0) + max(poldoPrev, default=0) + 1, end=" ")
    # print()
