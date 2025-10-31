from collections import Counter, defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()
s = input()
# 슬라이싱 윈도우 알고리즘
# 각 인덱스를 기준점으로 해서 팰랜드롬의 최대 길이를 구한다.
# 기준점이 홀수가 있고, 짝수가 있다.
def expand(s : str, left : int, right : int) -> list:
    while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
        left -= 1
        right += 1
    return s[left + 1:right - 1]
palindrome = ''
for i in range(len(s)):
    palindrome = max(palindrome, expand(s, i, i + 1), expand(s, i, i + 2), key=len)
print(len(palindrome))