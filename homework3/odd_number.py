'''
求奇数、偶数之和
'''
i = 1
odd_result = 0
even_result = 0
# 求奇数之和
while i <= 100:
    if i % 2 != 0:
        odd_result += i
    i += 1
print("奇数之和为:", odd_result)

# 求偶数之和
for j in range(1, 101):
    if j % 2 == 0:
        even_result += j

print("偶数之和为:", even_result)
