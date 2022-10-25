import random

code_list = ' '
# 随机产生不同类型的验证码
for i in range(4):
    state = random.randint(1, 3)
    print(state)
    if state == 1:
        first_kind = random.randint(65, 90)
        random_uppercase = chr(first_kind)
        code_list = code_list + random_uppercase
    elif state == 2:
        second_kinds = random.randint(97, 122)
        random_lowercase = chr(second_kinds)
        code_list = code_list + random_lowercase
    elif state == 3:
        third_kinds = random.randint(0, 9)
        code_list = code_list + str(third_kinds)
print(code_list)
