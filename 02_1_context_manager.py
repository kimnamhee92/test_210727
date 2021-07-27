"""
Context Manager Annotation
keyword : contextlib.contextmanager, __enter__, __exit__
"""
"""
With 구문 이해 : Contextlib 데코레이터 사용
코드 직관적, 예외 처리 용이
"""

import contextlib
import time

# Ex 1
# Use decorator
@contextlib.contextmanager
def file_writer(file_name, method):
    f = open(file_name, method)
    yield f  ## __enter__
    f.close() ## __exit__


with file_writer("./Python_lvl3/test_01.txt", 'w') as f:
    f.write('Context Manager Test4. \nContextlib Test4')


def num_generator(lst):
    for i in lst:
        yield i

t = num_generator([1,2,3,4,5])
print(t.__next__())
print(t.__next__())
print(t.__next__())

import sys, re
print(sys.path)
print([i for i in sys.path if re.search("pandas", i)])
