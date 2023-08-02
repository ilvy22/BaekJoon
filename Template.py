import sys
from copy import deepcopy
from heapq import heappush, heappop
from collections import deque, Counter
from itertools impor combinations
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

def count_by_range(arr, l, r):
    return bisect_right(arr, l, r) - bisect_left(arr, l, r)

def binary_search(arr, t, s, e):
    while s <= e:
        m = int((s + e) / 2)
        if arr[m] == t:
            return m
        elif arr[m] > t:
            e = m - 1
        else:
            s = m + 1
    
    return None