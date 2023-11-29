import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
last_digit_with_sign = -last_digit if number < 0 else last_digit

print("Last digit of {}, is {}, ".format(number, last_digit_with_sign), end=" ")


if last_digit_with_sign > 5:
    print ("and is greater than 5")
    
elif last_digit_with_sign == 0:
    print ("and is 0")
    
else:
    print ("and is less than 6 and not 0")



