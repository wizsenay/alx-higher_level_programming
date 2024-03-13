#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
copy_num = 0
last_num = 0
str_num = f'{number}'
for i in str_num:
    last_num = i
copy_num = int(last_num)
if number < 0:
    copy_num = copy_num * -1
print(f"Last digit of {number} is {copy_num}", end=" ")
if copy_num > 5:
    print("and is greater than 5")
elif copy_num == 0:
    print("and is 0")
elif copy_num < 6 and copy_num != 0:
    print("and is less than 6 and not 0")
