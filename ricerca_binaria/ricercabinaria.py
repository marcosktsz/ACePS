def binSearch(lower, upper):
    medium = (lower + upper) // 2
    print(f"?{medium}")
    reply = input()
    if reply == "=":
        return medium
    elif reply == "<":
        return binSearch(lower, medium - 1)
    else:
        return binSearch(medium + 1, upper)


T = int(input())

for _ in range(T):
    [n, k, b] = list(map(int, input().split()))
    if n == 1:
        print("!1", flush=True)
    if b == 0:
        print(f"!{binSearch(1, n)}", flush=True)
