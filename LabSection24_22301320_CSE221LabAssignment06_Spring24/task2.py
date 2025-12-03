import heapq
with open("input2_2.txt", "r") as file_input:
    N, M = map(int, file_input.readline().split())

    list_edges = []

    for i in range(M):
        u, v, w = map(int, file_input.readline().split())
        list_edges.append((u, v, w))


    A, B = map(int, file_input.readline().split())


def dijkstra(start, graph):
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    priorityQueue = [(0, start)]

    while priorityQueue:
        curr_distance, curr_node = heapq.heappop(priorityQueue)
        if curr_distance > distance[curr_node]:
            continue
        for neighbor, weight in graph[curr_node]:
            new_dist = curr_distance + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(priorityQueue, (new_dist, neighbor))

    return distance


graph = [[] for _ in range(N + 1)]
reversed_graph = [[] for _ in range(N + 1)]
for u, v, w in list_edges:
    graph[u].append((v, w))
    reversed_graph[v].append((u, w))

distanceOfAliceNode = dijkstra(A, graph)
distanceOfBobNode = dijkstra(B, reversed_graph)


min_time = float('inf')
meet_point = -1
for i in range(1, N + 1):
    max_time = max(distanceOfAliceNode[i], distanceOfBobNode[i])
    if max_time < min_time:
        min_time = max_time
        meet_point = i

with open("output2_2.txt", "w") as file_output:
    if min_time == float('inf'):
        file_output.write("Impossible\n")
    else:
        file_output.write(f"{min_time} {meet_point}\n")

