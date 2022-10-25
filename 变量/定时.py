import time
import datetime

curreent_time = datetime.datetime(2022, 10, 9, 21, 30)
t_next = datetime.datetime(2022, 10, 10, 00, 00)
date1 = datetime.timedelta(seconds=10)
now = datetime.datetime.now()
print(datetime.datetime.now())

print(now + date1)
# print(curreent_time)

touple = ('xiaoliu', '小花', 1)

touple1 = touple[1:]
print(touple[0])
print(touple1)

print("-" * 20)
for i in touple:
    print(i)

print(touple + touple1)
print("=" * 10)
print(id(touple))
touple = touple * 2
print(id(touple))
print(touple)

print(touple * 2)

print('小花' in touple)

list1 = list(touple)
print(list1)

touple2 = tuple(list1)
print(touple2)
