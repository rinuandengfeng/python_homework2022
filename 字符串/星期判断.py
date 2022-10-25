letter = input("请输入第一个字母：")
if letter == 'S':
    letter = input("请输入第二个字母：")
    if letter == 'a':
        print('Saturday')
    elif letter == 'u':
        print('Sunday')
    else:
        print("输入字母错误！")
elif letter == 'F':
    print('Friday')
elif letter == 'M':
    print('Monday')
elif letter == 'T':
    letter = input("请输入第二个字母：")
    if letter == 'u':
        print('Tuesday')
    elif letter == 'h':
        print('Thursday')
    else:
        print("输入字母错误！")
elif letter == 'W':
    print('Wednesday')
else:
    print("输入字母错误！")