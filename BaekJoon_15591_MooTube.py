# https://www.acmicpc.net/problem/15591
# MooTube (Silver) 

import sys
from collections import deque
input = sys.stdin.readline

def BFS(k, v):
	visit = [0] * (N+1)
	q = deque()
	q.append((v, int(1e9))) # Node, Cost
	visit[v] = 1
	cnt = 0
	
	while q:
		now, cost = q.popleft()
		for nxt, c in g[now]:
			# print(nxt, c)
			ncost = min(cost, c)
			if visit[nxt] == 1: continue
			
			q.append((nxt, ncost))
			visit[nxt] = 1
			# print(ncost)

			if ncost >= k:
				cnt += 1
	
	return cnt
	
	# print(cnt)
	

N, Q = map(int, input().split())
g = [[] for _ in range(N+1)]
for _ in range(N-1):
	a, b, c = map(int, input().split())
	g[a].append((b, c))
	g[b].append((a, c))

	
for _ in range(Q):
	k, v = map(int, input().split())
	print(BFS(k, v))