# https://www.acmicpc.net/problem/2805
# 나무자르기

import sys
input = sys.stdin.readline

def Solve():
	global ans
	
	s = 1
	e = L[-1]
	
	while s <= e:
		m = int((s + e) / 2)
		if sum([i - m for i in L if i - m >= 0]) >= M:
			ans = m
			s = m + 1
		else:
			e = m - 1
	

N, M = map(int, input().split())
L = list(map(int, input().split()))
L.sort()

ans = 0
Solve()
print(ans)