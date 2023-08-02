# https://www.acmicpc.net/problem/1654
# 랜선 자르기

import sys

input = sys.stdin.readline

def Solve():
	
	s = 1
	e = max(L)
	
	while s <= e:
		m = int((s + e) / 2)
		if sum([int(i/m) for i in L]) >= M:
			s = m + 1
		
		else:
			e = m -1
	
	return e
	

N, M = map(int, input().split())
L = [int(input())for _ in range(N)]
L.sort()
# print(L)

ans = Solve()
print(Solve())
