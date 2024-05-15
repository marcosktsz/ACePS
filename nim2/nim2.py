def play(m, n):
    while m != 1 and n != 1:
        print(f"{min(m,n)} {min(m,n)}")
        [m, n] = list(map(int, input().split()))
    print("1 1")


T = int(input())

for _ in range(T):
    [m, n] = list(map(int, input().split()))
    if m == n:
        print(2)
        [m, n] = list(map(int, input().split()))
        play(m, n)
    else:
        print(1)
        play(m, n)
