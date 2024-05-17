from collections import deque

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    graph = {i: [] for i in range(n)}

    for _ in range(m):
        s, d = map(int, input().split())
        graph[s].append(d)
        graph[d].append(s)

    visited = [
        set(),
        set(),
    ]

    visited[0].add(0)

    queue = deque([(0, [])])

    found = False

    while queue:
        current, path = queue.popleft()
        current_len = len(path)
        if current == 0 and current_len % 2 != 0:
            print(current_len)
            print(" ".join(map(str, [0] + path)))
            found = True
            break
        for neighbor in graph[current]:
            if neighbor not in visited[(current_len + 1) % 2]:
                queue.append((neighbor, path + [neighbor]))
                visited[(current_len + 1) % 2].add(neighbor)

    if not found:
        print(0)
        print(0)
