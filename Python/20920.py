from collections import Counter
import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
# 단어장 생성
words = [input() for _ in range(N)]
# 길이가 M 이상인 단어만 필터링
words = [word for word in words if len(word) >= M]
# 단어 빈도수 계산
wordsCount = Counter(words)
# 빈도수, 길이, 사전순으로 정렬하기
words.sort(key = lambda x: (-wordsCount[x], -len(x), x))
# 중복 제거 후 출력
newWords = list(set(words))
for word in newWords:
    print(word)
