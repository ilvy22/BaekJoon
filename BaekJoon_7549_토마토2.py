# https://www.acmicpc.net/problem/7569
# 토마토2

import sys
from collections import deque
input = sys.stdin.readline

def BFS():
	cnt = len([(h, n, m) for h in range(H) for n in range(N) for m in range(M) if b[h][n][m] == 0])	
	if cnt == 0: return cnt
	
	q = deque([(h, n, m, 0) for h in range(H) for n in range(N) for m in range(M) if b[h][n][m] == 1])	
	
	while q:
		x, y, z, time = q.popleft()
		for dx, dy, dz in d:
			nx, ny,nz, ntime = x + dx, y + dy, z + dz, time + 1
			
			if not 0 <= nx < H: continue
			if not 0 <= ny < N: continue
			if not 0 <= nz < M: continue
			if b[nx][ny][nz] != 0: continue
			
			b[nx][ny][nz] = ntime
			cnt -= 1
			q.append((nx, ny, nz, ntime))
			
			if cnt == 0:
				return ntime
	
	return -1
		

M, N, H = map(int, input().split())	# 열, 행, 높이
b = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
d = ((0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0))

ans = BFS()
print(ans)
