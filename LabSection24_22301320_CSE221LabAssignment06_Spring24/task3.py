with open("input3_1.txt", "r") as file_input:
    N, M = map(int, file_input.readline().split())

    list_edges = []

    for _ in range(M):
        u, v, w = map(int, file_input.readline().split())
        list_edges.append((u, v, w))

def safePath(x):
    visited = [False] * (N + 1)
    stack = [1]

    while stack:
        curr = stack.pop()
        if curr == N:
            return True
        if visited[curr]:
            continue
        visited[curr] = True

        for u, v, w in list_edges:
            if u == curr and w <= x and not visited[v]:
                stack.append(v)
            elif v == curr and w <= x and not visited[u]:
                stack.append(u)

    return False


low, high, result = 1, 100, -1

while low <= high:
    mid = (low + high) // 2
    if safePath(mid):
        result = mid
        high = mid - 1
    else:
        low = mid + 1

with open("output3_1.txt", "w") as file_output:
    if result == -1:
        file_output.write("Impossible\n")
    else:
        file_output.write(f"{result}\n")
