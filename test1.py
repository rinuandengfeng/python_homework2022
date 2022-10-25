# # x = input()
#
# # a = int((x+10)*8/2//3 % 10)
# # a = a ** 3
# # print(a)
#
#
# list1 = [1,2,3,4]
# # list1.extend(1)
# print(list1)
#
# list = [1,2,3,4,5]
#
# list.append(6)
#
# print(list)
#
# list1,list2 = [1,2,3],[4,5,6]
# list1.extend(list2)
# print(list1)
#
#
# list1 = [1,2,3,4]
#
# list1.insert(1,6)
# print(list1)
#
#
# list1 = ['a',1,2,3]
#
# x = list1.pop()
#
# print(list1)   #
#
# print(x)
#
#
# list1 = ['a',1,2,3,1]
# list1.remove(1)
# print(list1)
#
#
# list1 = [1,2,3,4,5]
#
# list1.clear()
#
# print(list1)
#
#
# list1 = [1,2,3,4,5]
#
# print(list1.index(3))
#
# list1 = [3,5,6,1,2,9]
#
# list1.sort()
#
# print(list1)
#
# list1.sort(reverse = True)
#
# print(list1)
#
#
# list1 = [4,3,1,6,7]
#
# list1.reverse()
#
# print(list1)
#
# list1 = [1,2,3,4,1,2,1,2,1]
#
# x = list1.count(1)
#
# print(x)
#
# list1 = [1,2,3,4]
#
# list2 = [nums ** 2 for nums in list1]
#
# print(list2)
#
# list1 = [1,2,3,4,5]
#
# list2 = [num ** 2 for num in list1 if num >2]
#
# print(list2)
#
#
#

class Foo():

    def __init__(self):
        pass

    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]


foo = Foo()

print(foo[0])


lists = [1,2,3,4]
a = lists.copy()
a[2] =8
print(lists)
print(a)