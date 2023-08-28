# https://www.acmicpc.net/problem/9205
# 맥주마시면서걸어가기

import sys
from collections import deque
input = sys.stdin.readline

def BFS():
	ans = 'sad'
	q = deque()
	q.append((sx, sy))

	
	while q:
		x, y = q.popleft()
		# print(x, y)
		if abs(fx - x) + abs(fy - y) <= 1000:
			return "happy"
		
		for i in range(N):
			nx, ny = Conv[i]
			# print(nx, ny)
			if v[i] == 1: continue
			if abs(nx-x) + abs(ny-y) > 1000: continue
			
			q.append((nx, ny))			
			# print(nx, ny)
			v[i] = 1
	
	return ans

T = int(input())
for k in range(T):
	N = int(input())
	sx, sy = map(int, input().split())
	Conv = []	
	for _ in range(N):
		x, y = map(int, input().split())
		Conv.append((x, y))
	fx, fy = map(int, input().split())	
	
	v = [0] * (N+1)	
	# print(k)
	print(BFS())
	
