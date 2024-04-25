import random
import string

all_sign = string.ascii_letters + string.digits
print(all_sign)
count = ''
for i in range(6):
    count += random.choice(all_sign)
print("生成的6位验证码为%s" % count)




