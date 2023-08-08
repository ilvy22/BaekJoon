# https://www.acmicpc.net/problem/2110
# 공유기 설치

import sys
input = sys.stdin.readline

def Solve():
	global ans
	
	s = 1
	e = arr[-1]	
	
	while s <= e:
		m = (s + e) // 2
		val = arr[0]
		cnt = 1
		
		for i in range(1, N):
			if arr[i] >= val + m:
				val = arr[i]
				cnt += 1
		
		if cnt >= C:
			s = m + 1
			ans = m
		else:
			e = m - 1
		

N, C = map(int, input().split())
arr = []
for _ in range(N):
	arr.append(int(input()))
arr.sort()
	
# print(f'{N}, {C}, {D}')

ans = 0
Solve()
print(ans)