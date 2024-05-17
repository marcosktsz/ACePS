def play(m, n):
    while m != 1 and n != 1:
        print(f"{min(m,n)} {min(m,n)}", flush=True)
        [m, n] = list(map(int, input().split()))
    print("1 1")


T = int(input())

for _ in range(T):
    [m, n] = list(map(int, input().split()))
    if m == n:
        print(2, flush=True)
        [m, n] = list(map(int, input().split()))
        play(m, n)
    else:
        print(1, flush=True)
        play(m, n)
