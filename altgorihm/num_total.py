num =[]
while True:
    try:
        num.append(int(input()))
    except:
        break
total = 0
for i in num:
    for j in range(1,i+1):
        total += j
    print(total)
    total = 0