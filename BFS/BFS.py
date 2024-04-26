T = int(input())

for _ in range(T):
    [v, e] = list(map(int, input().split()))
    graph = {i: [] for i in range(v)}
    childNodes = {i: [] for i in range(v)}
    for i in range(e):
        [u, v] = list(map(int, input().split()))
        graph[u].append(v)
        childNodes[v].append(u)

    visited = [0]
    queue = [[0, 0]]

    distances = [0 for _ in range(len(graph))]
    parents = [0 for _ in range(len(graph))]

    while queue:
        current = queue.pop(0)
        for n in graph[current[0]]:
            if n not in visited:
                distances[n] = current[1] + 1
                parents[n] = current[0]
                visited.append(n)
                queue.append([n, current[1] + 1])

    for distance in distances:
        print(distance, end=" ")
    print()
    for parent in parents:
        print(parent, end=" ")
    print()
    childNodes.pop(0)

    count = 1
    for child, parents in childNodes.items():
        dis = []
        for parent in parents:
            dis.append(distances[parent])
        comb = dis.count(min(dis))
        count *= comb
    print(count % 1000000007)
