import sys
input = sys.stdin.readline
n = int(input().strip())
for _ in range(n):
    sentence = input().strip().lower()
    is_palindrome = True
    # sentence == sentence[::-1]
    is_palindrome = sentence == sentence[::-1]
    if is_palindrome:
        print("Yes")
    else:
        print("No")
    
# Problem: 10174 - Palindrome Headache