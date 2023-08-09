# https://www.acmicpc.net/problem/2468
# 안전 영역

import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def BFS(i, j, k, v):
	cnt = 0
	
	q = deque()
	q.append((i, j))
	v[i][j] = 1
	
	while q:
		x, y = q.popleft()
		for dx, dy in d:
			nx, ny = x + dx, y + dy
			
			if not 0 <= nx < N: continue
			if not 0 <= ny < N: continue
			if v[nx][ny]: continue
			if b[nx][ny] <= k: continue
			
			q.append((nx, ny))
			v[nx][ny] = 1
	

def Solve():
	global ans	
	maxVal = max(map(max, b))
	
	for k in range(0, maxVal + 1):
		v = [[0] * (N+1) for _ in range(N+1)]
		cnt = 0
		
		for i in range(N):
			for j in range(N):
				if v[i][j] == 0 and b[i][j] > k:
					BFS(i, j, k, v)
					cnt += 1
		
		ans = max(ans, cnt)
		
	

N = int(input())
b = [list(map(int, input().split())) for _ in range(N)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))

ans = 0
Solve()
print(ans)