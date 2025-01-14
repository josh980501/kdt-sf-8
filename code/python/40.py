# 솔루션 1
# 실습. 로또 번호 뽑기

import random

lotto = sorted(random.sample(range(1, 46), 6))

print(lotto) # window + f2

# 솔루션 2
# 1. 빈 set 만들기
lotto_nums = set()

# 2. 6개의 숫자 뽑기
while len(lotto_nums) < 6:
    # 난수를 set에 추가
    lotto_nums.add(random.randint(1, 45))

# 3. 오름 차순 정렬
sorted_lotto_nums = sorted(lotto_nums)
print(sorted_lotto_nums)