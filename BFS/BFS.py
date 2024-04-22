T = int(input())

for _ in range(T):
    [v, e] = list(map(int, "".join(input().split())))
    graph = {i: [] for i in range(v)}
    for i in range(e):
        [u, v] = list(map(int, "".join(input().split())))
        graph[u].append(v)

    visited = [0]
    queue = [[0, 0]]

    distances = [0 for _ in range(len(graph))]
    parents = [0 for _ in range(len(graph))]
    nTrees = 0

    while queue:
        current = queue.pop(0)

        for n in graph[current[0]]:
            if n not in visited:
                nTrees = nTrees + 1
                distances[n] = current[1] + 1
                parents[n] = current[0]
                visited.append(n)
                queue.append([n, current[1] + 1])
    print(distances)
    print(parents)
    print((nTrees - 1) % 1000000007)
