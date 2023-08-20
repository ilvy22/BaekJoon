# https://www.acmicpc.net/problem/2667
# 단지번호붙이기

import sys
from collections import deque
input = sys.stdin.readline

def BFS(i, j):
	q = deque()
	q.append((i, j, 0))	
	v[i][j] = 1
	cnt = 1
	
	while q:
		x, y, time = q.popleft()
		for dx, dy in d:
			nx, ny, ntime = x + dx, y + dy, time + 1
						
			if not 0 <= nx < N: continue	# 범위 조건
			if not 0 <= ny < N: continue	# 범위 조건
			if v[nx][ny] == 1: continue		# 방문 여부
			if b[nx][ny] == 0: continue		# 값 조건
			
			v[nx][ny] = 1
			cnt += 1
			q.append((nx, ny, ntime))
			
			# print(nx, ny, ntime)			
	return cnt
			

N = int(input())
b = [list(map(int, input().strip())) for _ in range(N)]
v = [[0] * (N+1) for _ in range(N+1)]
d = ((0, 1), (1, 0), (0, -1), (-1, 0))

ans = [BFS(i, j) for i in range(N) for j in range(N) if b[i][j] == 1 and v[i][j] == 0]
ans.sort()
print(len(ans))
print(*ans)