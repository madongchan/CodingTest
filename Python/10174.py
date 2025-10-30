import sys
input = sys.stdin.readline
n = int(input().strip())
for _ in range(n):
    sentence = input().strip().lower()
    # two pointers
    left, right = 0, len(sentence) - 1
    is_palindrome = True
    
# Problem: 10174 - Palindrome Headache