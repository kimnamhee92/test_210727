print('-' * 30)

a = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda x: x*2, a)))

even_squares = [x**2 for x in a if x %2 ==0]
print(even_squares)

alt = map(lambda x: x**2, filter(lambda x : x%2 ==0, a))
print(">>> {}".format(list(alt)))

#print(alt)


#####################################################################
from itertools import islice

def fib():
    prev, curr = 0, 1
    while True:
        prev, curr = curr, prev + curr
        yield curr

f = fib()

print(list(islice(f, 0, 10)))

class test:
    '''test1'''
    def __init__(self, name, age, *args):
        self.name = name
        self.age = age
        self.lst = list(args)
        print('init >> name : {}, age : {}, etc : {}'.format(self.name, self.age, self.lst))

    def __call__(self):
        print('call >> hi~!')

    def __str__(self):
        '''hello this is str'''
        return 'str >> {} is {}'.format(self.name, self.age)

    def __repr__(self):
        ''' repr test '''
        return 'repr >> {} _ {}'.format(self.name, self.age)


hee = test('namhee',28, [1,2,3]) ## __init__ : 객체 초기화
print("-"* 48)
print(hee()) ## __call__ : 인스턴스 생성


#t = test('namhee', 28, "a", "b", "c")
#print(t.lst.__len__())

####################################################################

import pandas as pd
import re

lst = [1,2,3]
lst = pd.Series(lst)
print(dir(lst))
print(">> Series dir :\n", list(filter(lambda i: not re.search("_", i), dir(lst))) )

#####################################################################
