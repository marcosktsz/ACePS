def askMed(a, b, c):
    print(a - 1, b - 1, c - 1)
    res = int(input())
    return res + 1


def findPos(x, s, d):
    s3 = s + (d - s) // 3
    d3 = s + (2 * (d - s) + 1) // 3

    assert s <= d

    if s == d:
        if s != 0:
            s -= 1
        else:
            d += 1

    if d == s + 1:
        t = askMed(support[s], support[d], x)
        if t == x:
            return d
        elif t == support[s]:
            return s
        else:
            return d + 1

    t = askMed(support[s3], support[d3], x)

    if t == x:
        if s3 + 1 == d3:
            return d3
        return findPos(x, s3 + 1, d3 - 1)

    if t == support[s3]:
        if s == s3:
            return s
        return findPos(x, s, s3 - 1)

    if d3 == d:
        return d + 1
    return findPos(x, d3 + 1, d)


T = int(input())
for _ in range(T):
    N = int(input())

    support = [i for i in range(N)]

    if N == 3:
        print(0, 1, 2)
        print(int(input()))
    elif N == 1:
        print(0)
    else:
        i = askMed(1, 2, 3)
        support[1] = i

        if i == 1:
            support[0] = 2
            support[2] = 3
        elif i == 2:
            support[0] = 1
            support[2] = 3
        else:
            support[0] = 1
            support[2] = 2

        l = 3
        for i in range(4, N + 1):
            if i > (N + 1) // 2 + 1:
                support = support[1:l]
                l -= 2

            if l == 1:
                break

            t = findPos(i, 0, l - 1)
            support[t + 1 : l + 1] = support[t:l]
            support[t] = i
            l += 1

        print(support[l // 2] - 1)
