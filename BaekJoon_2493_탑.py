# https://www.acmicpc.net/problem/2493
# 탑

import sys
from collections import deque
input = sys.stdin.readline

def Solve():
	ans = [0] * N
	stack = deque()
	for i in range(N):		
		while stack:
			if stack[-1][1]	> L[i]:
				ans[i] = stack[-1][0] + 1
				break
			else:
				stack.pop()
		
		if not stack: ans[i] = 0
		
		stack.append((i, L[i]))
			
	return ans


N = int(input())
L = list(map(int, input().split()))

ans = Solve()
print(*ans)