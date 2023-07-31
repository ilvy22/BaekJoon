# 다익스트라 알고리즘 소스코드


import sys
import heapq
from collections import deque

readl = sys.stdin.readline
INF = int(1e9)

N, M = map(int, readl().split())
S = int(readl())
g = [[] for _ in range(N+1)]
d = [INF] * (N+1)

for _ in range(M):
	a, b, c = map(int, readl().split())
	g[a].append((b, c))

def dijkstra(S):
	q = []
	heapq.heappush(q, (0, S))
	d[S] = 0
	
	while q:
		dist, now = heapq.heappop(q)
		if d[now] < dist:
			continue
			
		for dst, cost in g[now]:
			nc = dist + cost
			if nc < d[dst]:
				d[dst] = nc
				heapq.heappush(q, (nc, dst))
				
dijkstra(S)

for i in range(1, N+1):
	if d[i] == INF:
		print("INF")
	else:
		print(d[i])