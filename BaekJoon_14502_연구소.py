# https://www.acmicpc.net/problem/14502
# 연구소

import sys;	input = sys.stdin.readline
import copy
import heapq
from collections import deque
from itertools import combinations

def Solve():
	global ans
	for combi in combinations(empty, wall_n):
		board_new = copy.deepcopy(board)
		for x_w, y_w in combi:
			board_new[x_w][y_w] = 1
			
		virus = [(n, m) for n in range(N) for m in range(M) if board_new[n][m] == 2]
		
		while virus:
			x_v, y_v = virus.pop()
			for dx, dy in d:
				nx = x_v + dx
				ny = y_v + dy
				
				if 0 <= nx < N and 0 <= ny < M and board_new[nx][ny] == 0:
					board_new[nx][ny] = 2
					virus.append((nx, ny))
					
		
		cnt = 0
		for row in board_new:
			cnt += row.count(0)
		
		ans = max(cnt, ans)
		



N, M = map(int, input().split())
wall_n = 3
board = [list(map(int, input().split())) for _ in range(N)]
empty = [(n, m) for n in range(N) for m in range(M) if board[n][m] == 0]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0
Solve()
print(ans)