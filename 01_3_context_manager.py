## Context Manager
# contextlib, __enter__, __exit__, exception
# with 구현
"""
컨텍스트 매니저 : 원하는 타이밍에 정확하게 리소스 할당 및 제공, 반환하는 역할
- 가장 대표적 with 구문 이해 : 자동 자원 반환
"""
# Ex 1
f = open("./Python_lvl3/testfile.txt", 'w')
try:
    f.write("context manager test\ncontextlib test1")
finally:
    f.close()

# Ex 2
with open("./Python_lvl3/testfile2.txt",'w') as f
    f.write("context manager test\ncontextlib test2")

# Ex 3
## Use Class -> context manager with exception handling.

## class 선언
class MyFileWriter():
    def __init__(self, file_name, method):
        print("MyFileWriter started : __init__")
        self.file_obj = open(file_name, method)
    # __enter__ 와 __exit__ 메소드를 선언하면 context manager로 작동!
    def __enter__(self):
        print('MyFileWriter started : __enter__')
        return self.file_obj

    def __exit__(self, exc_type, value, trace_back):
        print('MyFileWriter started : __exit__')
        if exc_type:
            print("Logging exception {}".format((exc_type, value, trace_back)))
        self.file_obj.close()

with MyFileWriter("./Python_lvl3/testfile3.txt", "w") as f:
    f.write("context manager test\ncontextlib test3")


################################################################################
"""
Context manager -> contextlib, __enter__, __exit__
Contextlib -> Measure execution(타이머)
"""

# Ex 1
# Use class

import time

class ExcuteTimer(object):
    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        self._start = time.monotonic()
        return self._start

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print("Logging exception {}".format((exc_type, exc_value, exc_traceback)))
        else:
            print("{} : {} s".format(self._msg, time.monotonic() - self._start))
        return True

with ExcuteTimer('Start! job') as v:
    print('Receive start monotonic1 : {}'.format(v))
    for i in range(100):
        pass
    raise Exception('Raise! Exception!')
