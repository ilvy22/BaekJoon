# https://www.acmicpc.net/problem/2467
# 용액

import sys
input = sys.stdin.readline

def Solve():
		
	left_idx = 0
	right_idx = N-1
	
	ans = abs(L[left_idx] + L[right_idx])
	ans_left = left_idx
	ans_right = right_idx
	
	while left_idx < right_idx:
		temp = L[left_idx] + L[right_idx]
		if abs(temp) < ans:
			ans_left = left_idx
			ans_right = right_idx
			ans = abs(temp)
		
		if temp < 0:
			left_idx += 1
		else:
			right_idx -= 1
	
	return L[ans_left], L[ans_right]
	

N = int(input())
L = list(map(int, input().split()))

left, right = Solve()
print(left, right)
