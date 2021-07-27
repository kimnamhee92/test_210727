"""
Functions : Lambda, Reduce, Map, Filter

"""
"""
lambda 장점 : 익명, 힙(heap) 메모리 영역에서 사용 즉시 소멸!, 가비지 컬렉션
일반함수 : 재사용성 위한 메모리 저장
시퀀스형 전처리에 Reduce, Map, Filter 주로 사용
cf. Reduce : 순환 -> 단일 변수 값으로 반환
"""
from functools import reduce

digits = [x for x in range(1,101)]

result = reduce(lambda x, y : x+y, digits)

print(result)


"""
객체 복사의 종료 : copy, Shallow copy, Deep copy
정확한 이해 후 사용
- mutable : list, set, dict 에 대한 copy
  (cf. immutable : int, str, float, bool, unicode ... )
"""

# Ex 1 - copy
# Call by value, Call by Reference, Call by Share
## 주소 값 and 값을 넘김

a_lst = [1,2,3, [4,5,6], [7,8,9]]
b_lst = a_lst

print('just allocate a >', id(a_lst))
print('just allocate b >', id(b_lst))

b_lst[2] = 100
print('just allocate a >', a_lst)
print('just allocate b >', b_lst)

# Ex 2 - Shallow-copy >> import copy : copy.copy()
## 중첩 리스트 (리스트 내 리스트)는 call by reference로 값의 주소값 같음!

import copy

c_lst = [1,2,3, [4,5,6], [7,8,9]]
d_lst = copy.copy(c_lst)

print('copy func c > ', id(c_lst))
print('copy func d > ', id(d_lst))

# Ex 3 - Deep copy

e_lst = [1,2,3, [4,5,6], [7,8,9]]
f_lst = copy.deepcopy(e_lst)

print('copy func e > ', id(e_lst))
print('copy func f > ', id(f_lst))

f_lst[3].append(1000)
f_lst[4][1] = 10000

print('just allocate e >', e_lst)
print('just allocate f >', f_lst)
