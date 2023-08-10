# https://www.acmicpc.net/problem/4673
# 셀프 넘버

MAX = int(10000)

def Solve(i):
	return i + sum([int(s) for s in str(i)])

def binary_search(arr, t, s, e):
	while s <= e:
		m = (s+e) // 2
		if arr[m] == t:
			return m
		elif arr[m] > t:
			e = m - 1
		else:
			s = m + 1
	return None


notSelfNumber = [Solve(i) for i in range(MAX)]
notSelfNumber.sort()
for i in range(1, 10000+1):
	if binary_search(notSelfNumber, i, 1, 10000) == None:
		print(i)

