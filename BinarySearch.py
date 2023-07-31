# 이진 탐색 소스코드

import sys
input = sys.stdin.readline

def bi_srch(arr, t, s, e):
	while s <= e:
		m = int((s + e) / 2)
	
		if arr[m] == t:
			return m
		elif arr[m] > t:
			e = m - 1
		else:
			s = m + 1
			
	return None
		
n, target = map(int, input().split())
arr = list(map(int, input().split()))
ans = bi_srch(arr, target, 0, n-1)
print(ans)