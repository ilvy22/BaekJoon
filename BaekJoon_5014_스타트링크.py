# https://www.acmicpc.net/problem/5014
# 스타트링크

import sys
from collections import deque
input = sys.stdin.readline


F, S, G, U, D = map(int, input().split())	# S 현재 위치, G  목적지
d = (+U, -D)
v = [0] * (F + 1)
ans = -1

q = deque()
q.append((S, 0))
v[S] = 1

while q:
	now, time = q.popleft()
	
	if now == G:
		ans = time
		break
			
	for n in d:
		nxt, ntime = now + n, time + 1
		if not 1 <= nxt <= F: continue
		if v[nxt] == 1: continue
		
		v[nxt] = 1
		q.append((nxt, ntime))		
		
if ans == -1:
	print("use the stairs")
else:
	print(ans)
