# https://www.acmicpc.net/problem/1747
# 소수 & 팰린드롬

import sys
import math

MAX = int(1e9)

def PelindromNumer(x):
	if str(x) == str(x)[::-1]:
		return True
	else:
		return False

def PrimeNumber(x):
	if x == 1:
		return False
	for i in range(2, int(math.sqrt(x)) + 1):
		if x % i == 0:
			return False		
	return True

N = int(input())
for x in range(N, MAX):
	if PelindromNumer(x) and PrimeNumber(x):
        print(x)
        break
	