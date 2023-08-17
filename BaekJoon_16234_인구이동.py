# https://www.acmicpc.net/problem/16234
# 인구이동

import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

def BFS(i, j, v):
	
	q = deque()
	q.append((i, j))
	pos = []
	val = []
	pos.append((i, j))
	val.append((b[i][j]))
	
	v[i][j] = 1
	# print(i, j)
	# print(val)
	# print(pos)
	
	while q:
		x, y = q.popleft()
		for dx, dy in d:
			nx, ny = x + dx, y + dy
			
			if not 0 <= nx < N: continue
			if not 0 <= ny < N: continue
			if v[nx][ny] == 1: continue			
			if not L <= abs(b[x][y] - b[nx][ny]) <= R: continue
			
			# print(nx, ny)
			
			v[nx][ny] = 1
			q.append((nx, ny))
			pos.append((nx, ny))
			val.append((b[nx][ny]))
			
	# print(pos)
	
	for i in range(len(pos)):
		x = pos[i][0]
		y = pos[i][1]		
		# print(x, y)
		nb[x][y] = sum(val)//len(val)
		# print(nb[x][y])
		
	return len(pos)


def Solve():
	global ans, calcF, b
	
	day = 0
	
	while calcF:
		calcF = False
		v = [[0] * (N+1) for _ in range(N+1)]
		
		for i in range(N):
			for j in range(N):
				if v[i][j] == 0:
					# print(f'{i}, {j}, {b[i][j]}')
					if BFS(i, j, v) >= 2:
						calcF = True
		
		b = deepcopy(nb)
					
		if calcF == True:
			day += 1
	
	ans = day
					

N, L, R = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(N)]
nb = deepcopy(b)	# 인구이동 후를 표시할 지도
d = ((0, 1), (0, -1), (1, 0), (-1, 0))

calcF = True

ans = 0
Solve()
print(ans)