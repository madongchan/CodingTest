from collections import Counter
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
words = [input() for _ in range(N)]
print('\n'.join(sorted(set(words), key=lambda x: (len(x), x))))