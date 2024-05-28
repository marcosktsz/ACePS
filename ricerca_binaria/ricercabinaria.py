liarsAndHonests = []


def lyingBinSearch(lower, upper):
    if lower == upper:
        return lower
    medium = (lower + upper) // 2
    print(f"?{medium}")
    reply = input()
    if reply == "=":
        return medium
    elif reply == ">":
        return lyingBinSearch(lower, medium - 1)
    else:
        return lyingBinSearch(medium + 1, upper)


def binSearch(lower, upper):
    if lower == upper:
        return lower
    medium = (lower + upper) // 2
    print(f"?{medium}")
    reply = input()
    if reply == "=":
        return medium
    elif reply == "<":
        return binSearch(lower, medium - 1)
    else:
        return binSearch(medium + 1, upper)


def manyKBinSearch(lower, upper, iteration, k):
    if lower == upper:
        return lower
    medium = (lower + upper) // 2
    print(f"?{medium}")
    reply = input()
    if reply == "=":
        return medium
    lying = liarsAndHonests[iteration % k]

    if lying:
        if reply == "<":
            return manyKBinSearch(medium + 1, upper, iteration + 1, k)
        else:
            return manyKBinSearch(lower, medium - 1, iteration + 1, k)
    else:
        if reply == ">":
            return manyKBinSearch(medium + 1, upper, iteration + 1, k)
        else:
            return manyKBinSearch(lower, medium - 1, iteration + 1, k)


T = int(input())

for _ in range(T):
    [n, k, b] = list(map(int, input().split()))
    if n == 1:
        print("!1", flush=True)
    if k == 1:
        if b == 0:
            print(f"!{binSearch(1, n)}", flush=True)
        if b == 1:
            print("?1")
            if input() == "<":
                print(f"!{lyingBinSearch(1, n)}", flush=True)
            else:
                print(f"!{binSearch(1, n)}", flush=True)
    else:
        liarsAndHonests = []
        for _ in range(k):
            print("?1")
            reply = input()
            if reply == "<":
                liarsAndHonests.append(1)
            elif reply == ">":
                liarsAndHonests.append(0)
            else:
                print(1)
                break
        print(f"!{manyKBinSearch(1,n,0,k)}", flush=True)
