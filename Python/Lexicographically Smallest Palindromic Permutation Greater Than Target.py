from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        
        count = Counter(s)
        odd_count_chars = [char for char, cnt in count.items() if cnt % 2 == 1]
        if len(odd_count_chars) > 1:
            return ""

        half_counts = Counter()
        mid = ''
        for char, cnt in count.items():
            half_counts[char] = cnt // 2
            if cnt % 2 == 1:
                mid = char
        
        n = len(s)
        L = n // 2
        
        # [수정] target의 "앞 절반"만 비교 대상으로 사용
        target_half = target[:L]
        
        # [수정] 현재 만든 "앞 절반"을 문자열로 관리 (더 쉬움)
        self.result = None # 최종 정답 (찾으면 즉시 저장)

        # "가장 작은" 문자열로 채우는 헬퍼
        def get_smallest_suffix(counts):
            res = []
            for char_code in range(ord('a'), ord('z') + 1):
                char = chr(char_code)
                res.extend([char] * counts[char])
            return "".join(res)

        def find_next(index, current_counts):
            # 1. (가지치기) 이미 더 좋은 답을 찾았으면 중단
            if self.result:
                return

            # 2. Base Case: "앞 절반" 완성
            if index == L:
                half_str = "" # (이 베이스 케이스는 아래 로직에서 도달 안 함)
                P = mid + half_str[::-1] # (실제로는 P가 여기서 완성되지 않음)
                return 

            # --- 3. "더 큰" 문자 시도 ---
            # index 위치에 target_half[index]보다 큰 문자를 넣기
            
            # [수정] target_half가 L보다 짧을 수 있음 (n이 홀수일 때)
            # 이 경우 'a'부터 시도
            start_char_code = ord('a')
            if index < len(target_half):
                start_char_code = ord(target_half[index]) + 1
                
            for char_code in range(start_char_code, ord('z') + 1):
                char = chr(char_code)
                if current_counts[char] > 0:
                    # "더 큰" 문자를 찾았다!
                    new_counts = current_counts.copy()
                    new_counts[char] -= 1
                    
                    # 나머지는 "가장 작은" 것들로 채운다
                    suffix = get_smallest_suffix(new_counts)
                    
                    # "앞 절반" 완성
                    half_str = current_half + char + suffix
                    P = half_str + mid + half_str[::-1]
                    
                    # (중요) self.result를 업데이트 (최초의 답이므로 가장 작음)
                    self.result = P
                    return # 즉시 종료 (이게 정답임)

            # --- 4. "같은" 문자 시도 ---
            # (target_half 범위 내에서만 가능)
            if index < len(target_half):
                target_char = target_half[index]
                if current_counts[target_char] > 0:
                    current_counts[target_char] -= 1
                    
                    # (중요) 다음 경로 탐색
                    find_next(index + 1, current_counts)
                    
                    # (백트래킹)
                    current_counts[target_char] += 1
            
            # (이 로직은 'a'부터 'z'까지 탐색하는 것이 아님)
            # (find_next는 "target보다 큰" 것만 찾음)

        # [수정] 백트래킹을 "target과 다른 첫 번째 지점"에서만 시작
        
        # 1. "앞 절반"의 최소 팰린드롬을 먼저 만듦
        min_half_str = get_smallest_suffix(half_counts.copy())
        min_P = min_half_str + mid + min_half_str[::-1]
        
        # 2. 최소 팰린드롬이 target보다 크면, 그게 정답
        if min_P > target:
            return min_P

        # 3. 최소 팰린드롬이 target 이하라면, "다음 순열" 찾기
        
        # "앞 절반"의 순열을 백트래킹으로 탐색
        current_half_arr = [''] * L
        
        def backtrack_next(index, counts):
            if self.result: return # 정답 찾으면 종료

            if index == L:
                half_str = "".join(current_half_arr)
                P = half_str + mid + half_str[::-1]
                if P > target:
                    self.result = P # 최초의 답
                return

            for char_code in range(ord('a'), ord('z') + 1):
                char = chr(char_code)
                if counts[char] > 0:
                    current_half_arr[index] = char
                    counts[char] -= 1
                    
                    # --- [수정된 가지치기] ---
                    # 현재 "앞 절반" (prefix)
                    h_prefix = "".join(current_half_arr[:index+1])
                    
                    # 이 prefix로 만들 수 있는 "가장 큰" 팰린드롬 (P_worst)
                    temp_counts_copy = counts.copy()
                    worst_suffix = ""
                    for c_code in range(ord('z'), ord('a') - 1, -1):
                        c = chr(c_code)
                        worst_suffix += c * temp_counts_copy[c]
                    
                    h_worst = h_prefix + worst_suffix
                    P_worst = h_worst + mid + h_worst[::-1]
                    
                    # P_worst가 target보다 작으면, 이 경로는 가망 없음
                    if P_worst <= target:
                        counts[char] += 1 # 재료 복구
                        continue # 다음 char 시도

                    backtrack_next(index + 1, counts)
                    
                    if self.result: return # 정답 찾으면 종료
                    counts[char] += 1 # 재료 복구

        backtrack_next(0, half_counts.copy())
        return self.result if self.result else ""