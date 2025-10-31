from collections import defaultdict
import sys

input = lambda: sys.stdin.read().strip()  # 여러 줄 입력을 처리하도록 수정
anagrams = defaultdict(list)
for word in input().splitlines():
    anagrams[''.join(sorted(word))].append(word)
# 그룹의 크기가 큰 순서대로 정렬, 크기가 같을 때는 각 그룹에서 가장 사전 순으로 앞서는 단어의 사전 순으로 출력한다.
#anagrams.sort(key = lambda x: (-len(anagrams[x])))
groupAnagrams = sorted(anagrams.values(), key = lambda x: (-len(x), x[0]))
#print(groupAnagrams)
for group in groupAnagrams[:5]:
    #print(type(group))
    print(f"Group of size {len(group)}: {' '.join(sorted(list(set(group))))} .")