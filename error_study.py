try:
    print('try....')
    r = 10 /5
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print("finally...")
print("END")

'''
执行结果:
    try....
    result: 2.0
    finally...
    END
'''
"""
    try...except...except...else...finally执行机制
    主要是说明在没有错误的时候，会自动执行esle语句块。
"""
try:
    print("try...")
    r = 10 / int(2)
    print('result:',r)
except ValueError as e:
    print("ValueError:",e)
except ZeroDivisionError as e:
    print("ZeroDivisionError:",e)
else:
    print("no error!")
finally:
    print("finally...")
print("END...")

'''
执行结果:
    try...
    result: 5.0
    no error!
    finally...
    END...
'''
'''
    python内置模块logging记录错误信息。
'''
import logging
from signal import raise_signal
def foo(s):
    return 10/ int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print("END")

'''
执行结果:
ERROR:root:division by zero
Traceback (most recent call last):
  File "E:\python-study\error_study.py", line 56, in main
    bar('0')
  File "E:\python-study\error_study.py", line 52, in bar
    return foo(s) * 2
  File "E:\python-study\error_study.py", line 49, in foo
    return 10/ int(s)
ZeroDivisionError: division by zero
END
'''

"""
创建错误类，使用raise抛出错误实例。
"""

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value:%s'%s)
    return 10 / n

# foo('0')

print("-------------------------")
'''
执行结果:
Traceback (most recent call last):
  File "E:\python-study\error_study.py", line 91, in <module>
    foo('0')
  File "E:\python-study\error_study.py", line 88, in foo
    raise FooError('invalid value:%s'%s)
__main__.FooError: invalid value:0
'''


'''
raise语句的作用
    抛出错误
'''

def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value:%s'%s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

# bar()

'''
执行结果:
ValueError!
Traceback (most recent call last):
  File "E:\python-study\error_study.py", line 123, in <module>
    bar()
  File "E:\python-study\error_study.py", line 118, in bar
    foo('0')
  File "E:\python-study\error_study.py", line 113, in foo
    raise ValueError('invalid value:%s'%s)
ValueError: invalid value:0
'''


'''
raise将一种错误类型转化为另一种错误类型
'''

try:
    10/0
except ZeroDivisionError:
    raise ValueError('input error!')

'''
执行结果
Traceback (most recent call last):
  File "E:\python-study\error_study.py", line 146, in <module>
    raise ValueError('input error!')
ValueError: input error!
'''
