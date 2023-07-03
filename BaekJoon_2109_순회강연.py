# https://www.acmicpc.net/problem/2109
# 순회강연

import sys
import heapq

def InputData():
	readl = sys.stdin.readline
	N = int(readl())
	L = []
	for _ in range(N):
		L.append(list(map(int, readl().split() )))
	
	L.sort(key=lambda x:x[1])
	return N, L

def Solve():
	q = []
	ans = 0
	for pay, day in L:
		heapq.heappush(q, pay)
		if day < len(q):
			heapq.heappop(q)
			
	print(sum(q))


sol = -1
N, L = InputData()
# print(lst)
sol = Solve()
# print(sol)