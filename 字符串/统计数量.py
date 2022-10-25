str = input("请输入一行字符串：")
letters = 0
space = 0
digit = 0
others = 0
for c in str:
    # 判断字符串是不是纯字符
    if c.isalpha():
        letters += 1
    # 判断字符串中是否包含空格
    elif c.isspace():
        space += 1
    # 判断字符串是不是存数字
    elif c.isdigit():
        digit += 1
    # 为其他字符
    else:
        others += 1
print("字符串共有%d个英文字母，%d个空格，%d个数字，%d个其他字符。" % (letters, space, digit, digit))
