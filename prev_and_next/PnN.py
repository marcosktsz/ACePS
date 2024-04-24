import sys

sys.setrecursionlimit(100000)
pairs = []


def parentheses(size, history="", left=0, right=0):
    if left == right == size:
        pairs.insert(0, history)
    if left < size:
        parentheses(size, history + "(", left + 1, right)
    if right < left:
        parentheses(size, history + ")", left, right + 1)


def tilingPrev(string):
    k = len(string)

    if k <= 0:
        return ""
    next = string[:]
    while k:
        if next[k - 4 : k] == "[--]":
            next = next[: k - 4] + "[][]" + next[k:]
            break
        if next[k - 6 : k] == "[--][]":
            next = next[: k - 6] + "[][--]" + next[k:]
            break
        else:
            next = tilingPrev(string[: k - 4]) + "[--]" + next[k:]
            break
    if len(next) != len(string):
        return ""
    return next


def tilingNext(string):
    k = len(string)
    if k == 0:
        return ""
    next = string[:]
    while k:
        if next[k - 4 : k] == "[][]":
            next = next[: k - 4] + "[--]" + next[k:]
            break
        if next[k - 4 : k] == "[--]":
            if next[k - 6 : k - 4] == "-]":
                next = tilingNext(string[: k - 4]) + "[][]" + next[k:]
                break
            else:
                next = next[: k - 6] + "[--][]" + next[k:]
            break
        else:
            k -= 2

    if len(next) != len(string):
        return ""
    return next


def numbers(size, base, number):
    k = size - 1
    j = size - 1
    prev = number[:]
    while prev:
        if prev[k] > 0:
            prev[k] -= 1
            break
        else:
            prev[k] = base - 1
            k -= 1
            if k < 0:
                print()
                break
    print(" ".join(map(str, prev)))
    next = number[:]
    while next:
        if next[j] < base - 1:
            next[j] += 1
            break
        else:
            next[j] = 0
            j -= 1
    print(" ".join(map(str, next)))


T = int(input())

for _ in range(T):
    string = input()
    if "[" in string:
        size = int(len(string) / 2)
        print(tilingPrev(string))
        print(tilingNext(string))

    elif "(" in string:
        size = int(len(string) / 2)
        parentheses(size)
        for index, pair in enumerate(pairs):
            if string == pair:
                if index > 1:
                    print(pairs[index - 1])
                else:
                    print()
                if index < len(pairs) - 1:
                    print(pairs[index + 1])
                else:
                    print()
        pairs = []
    else:
        c = list(map(int, string.split()))
        base = max(c) + 1
        size = len(c)
        numbers(size, base, c)
        counts = []
