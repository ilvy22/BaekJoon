# https://www.acmicpc.net/problem/10026
# 적록색약

import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def BFS(i, j, v, k):
	board = deepcopy(b)
	
	if k == 1:
		board = deepcopy(b)
		for m in range(N):
			for n in range(N):
				if board[m][n] == 'G':
					board[m][n] = 'R'
	
	q = deque()
	q.append((i, j))
	color = board[i][j]
	v[i][j] = 1
	
	while q:
		x, y = q.popleft()
		for dx, dy in d:
			nx, ny = x + dx, y + dy
			
			if not 0 <= nx < N: continue
			if not 0 <= ny < N: continue
			if v[nx][ny] == 1: continue
			if board[nx][ny] != color: continue
				
			q.append((nx, ny))
			v[nx][ny] = 1
			
	

N = int(input())
b = [list(input().strip()) for _ in range(N)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))

ans = []

for k in range(2):
	v = [[0] * (N+1) for _ in range(N+1)]
	cnt = 0	
	for i in range(N):
		for j in range(N):
			if v[i][j] == 0:
				BFS(i, j, v, k)
				cnt += 1
	
	ans.append(cnt)
	
print(*ans)