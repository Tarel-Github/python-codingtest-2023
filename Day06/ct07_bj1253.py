# 백준 1253 좋다

import sys
input = sys.stdin.readline

N= int(input())
count = 0

A = list (map(int, input().split()))
A.sort()

for k in range(N):
    find = A[k]
    i = 0; j = N - 1
    while i < j:
        if A[i] + A[j] == find:
            if i != k and j != k:
                count += 1
                break
            elif i == k : i += 1
            elif j == k : j -= 1
        elif A[i] + A[j] < find:
            i += 1
        elif A[i] + A[j] > find:
            j -= 1
 
print(count)
