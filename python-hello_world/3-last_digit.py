import random
number = random.randint(-10000, 10000)

print ("The last number of {}, is {}".format(number, abs(number) % 10), end= "")

if abs(number) % 10 > 5:
    print (" is greater than 5")
    
elif abs(number) % 10 == 0:
    print (" and is 0")
    
else:
    print (" and is less than 6 and not 0")



