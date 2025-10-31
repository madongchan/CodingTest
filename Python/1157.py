from collections import Counter
import sys

input = lambda: sys.stdin.readline().rstrip()

# 1. 문장 입력 받기기
#실패 후 문제 분석: 대소문자 구분 없이 처리해야 함
sentence = input().upper()

# 2. Counter를 사용해 각 알파벳의 빈도를 계산합니다.
counter = Counter(sentence)

# 3. 가장 빈도가 높은 알파벳들을 찾습니다.
max_freq = max(counter.values())
candidates = [char for char, freq in counter.items() if freq == max_freq]
# 4. 결과 출력
if len(candidates) > 1:
    print("?")
else:
    print(candidates[0])