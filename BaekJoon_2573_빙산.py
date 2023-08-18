# https://www.acmicpc.net/problem/2573
# 빙산

import sys
from collections import deque
input = sys.stdin.readline

def BFS(i, j):
	q = deque()
	q.append((i, j))
	v[i][j] = 1
	
	while q:
		x, y = q.popleft()
		for dx, dy in d:
			nx, ny = x + dx, y + dy
			if not 0 <= nx < N: continue
			if not 0 <= ny < M: continue
			if B[nx][ny] == 0:
				sea[x][y] += 1
				
			if B[nx][ny] != 0 and v[nx][ny] == 0:
				q.append((nx, ny))
				v[nx][ny] = 1

		
N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]
# print(B)


d = ((0, 1), (0, -1), (1, 0), (-1, 0))
cnt = 0
year = 0



while cnt < 2:
	cnt = 0
	v = [[0] * (M+1) for _ in range(N+1)]
	sea = [[0] * (M+1) for _ in range(N+1)]
	pos = [(i, j) for i in range(N) for j in range(M) if B[i][j] != 0]
	
	for x, y in pos:
		if B[x][y] != 0 and v[x][y] == 0:
			BFS(x, y)
			cnt += 1
			
	for x, y in pos:
		B[x][y] = max(B[x][y] - sea[x][y], 0)
		
	if len(pos) == 0:
		year = 0
		break
	
	if cnt >= 2:
		break
		
	year += 1

print(year)