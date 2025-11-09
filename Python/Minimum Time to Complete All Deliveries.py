from typing import List
import math
class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        # d1: 드론1이 완료해야 할 총 배달 횟수
        # d2: 드론2이 완료해야 할 총 배달 횟수
        # r1: 드론 1의 휴식 주기
        # r2: 드론 2의 휴식 주기
        d1, d2 = d[0], d[1]
        r1, r2 = r[0], r[1]
        # 둘 중 하나라도 일할 수 있는 최소 시간 찾기
        # 최소공배수 구하기
        def get_lcm(a, b):
            return (a * b) // math.gcd(a, b) # 최소공배수 = (a * b) / 최대공약수
        lcm_val = get_lcm(r1, r2)
        def check(X):
            drone1_time = X - (X // r1) # 드론1이 일할 수 있는 시간
            drone2_time = X - (X // r2) # 드론2가 일할 수 있는 시간
            total_workable_time = X - (X // lcm_val) # 둘 중 하나라도 일할 수 있는 시간
            
            return (drone1_time >= d1 and 
                    drone2_time >= d2 and 
                    total_workable_time >= d1 + d2)
        
        low = 1
        high = (d1 + d2) * 2 # 최악의 경우, 모든 배달이 휴식 시간에 걸리는 경우
        answer = high

        while low <= high: # 이분 탐색
            mid = (low + high) // 2 # 중간 시간 설정
            
            if check(mid):
                # mid 시간이 가능하다면, 
                # 이게 정답일 수 있으니 저장하고
                answer = mid
                # "더 적은 시간(왼쪽)"도 가능한지 탐색
                high = mid - 1
            else:
                # mid 시간이 불가능하다면,
                # "더 많은 시간(오른쪽)"이 필요함
                low = mid + 1
                
        return answer