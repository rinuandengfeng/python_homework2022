'''
输入一个字符串，将字符串中所有字母全部后移一位，
最后一个字符移动到字符串开头
'''

raw_str = input("请输入字符串:")
end_str = raw_str[-1]
other_str = raw_str[:-1]
print(end_str + other_str)
