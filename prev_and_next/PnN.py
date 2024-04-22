tilings = []
pairs = []


def tiling(size, history=""):
    if size == 0:
        tilings.append(history)
    elif size == 1:
        tiling(size - 1, history + "[]")
    else:
        tiling(size - 1, history + "[]")
        tiling(size - 2, history + "[--]")


def parentheses(size, history="", left=0, right=0):
    if left == right == size:
        pairs.insert(0, history)
    if left < size:
        parentheses(size, history + "(", left + 1, right)
    if right < left:
        parentheses(size, history + ")", left, right + 1)


def numbers(input):
    print("")


T = int(input())

for _ in range(T):
    string = input()
    if "[" in string:
        size = int(len(string) / 2)
        tiling(size)
        for index, tiles in enumerate(tilings):
            if tiles == string:
                if index > 1:
                    print(tilings[index - 1])
                else:
                    print()
                if index < len(tilings) - 1:
                    print(tilings[index + 1])
                else:
                    print()
        tilings = []
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
        print()
