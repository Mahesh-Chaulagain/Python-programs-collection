#1 list comprehensions
squares = [x**2 for x in range(10)]
print(squares)


#2 Generator Expressions
squares_gen = (x**2 for x in range(10))
print(squares_gen)


#3 Default dictionary
from collections import defaultdict
dd = defaultdict(int)
dd['key'] += 1
print(dd)


#4 Named Tuples
from collections import namedtuple
Point = namedtuple('Point','x y')
p = Point(10,20)
print(p)


#5 Enumerate function
for index, value in enumerate(['a','b','c','d']):
    print(index, value)


#6 Zip function
names = ['a', 'b', 'c']
ages = [20, 25, 30]
combined = list(zip(names, ages))
print(combined)


#7 Set comprehensions
unique_squares = {x**2 for x in range(10)}
print(unique_squares)


#8 Frozenset
fs = frozenset([1,2,3,2,1])
# print(fs[0])


#9 Counter
from collections import Counter
counts = Counter(['a','b','c','a','c','b','c','a'])
print(counts)


#10 Context Managers
# with open('file.txt','r') as file:
#     contents = file.read()


#11 dataclass
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int


#12 Decorators
def my_decorator(func):
    def wrapper():
        print('something is happening before the function is called')
        func()
        print('something is happening after the function is called')
    return wrapper

@my_decorator
def say_hello():
    print('hello')

say_hello()


#13 Asyncio
import asyncio
async def main():
    print('hello')
    await asyncio.sleep(5)
    print('world!')

asyncio.run(main())