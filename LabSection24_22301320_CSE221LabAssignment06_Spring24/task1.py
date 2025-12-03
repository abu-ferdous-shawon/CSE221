import heapq

with open("input1_2.txt", "r") as file_input:
    N, M = map(int, file_input.readline().split())

    edges = []

    for i in range(M):
        u, v, w = map(int, file_input.readline().split())
        edges.append((u, v, w))

    S = int(file_input.readline())


distance = [float('inf')] * (N + 1)
distance[S] = 0

priorityQueue = [(0, S)]

graph = [[] for _ in range(N + 1)]
for u, v, w in edges:
    graph[u].append((v, w))


while priorityQueue:
    curr_distance, curr_node = heapq.heappop(priorityQueue)
    if curr_distance > distance[curr_node]:
        continue
    for neighbor, weight in graph[curr_node]:
        new_dist = curr_distance + weight
        if new_dist < distance[neighbor]:
            distance[neighbor] = new_dist
            heapq.heappush(priorityQueue, (new_dist, neighbor))

with open("output1_2.txt", "w") as file_output:
    for i in range(1, N + 1):
        if distance[i] == float('inf'):
            file_output.write("-1 ")
        else:
            file_output.write(str(distance[i]) + " ")


