# def validate_password(password):
#     # Check the length of the password
#     if len(password) < 8:
#         return False

#     # Check for at least one uppercase letter, one lowercase letter, and one digit
#     has_uppercase = False
#     has_lowercase = False
#     has_digit = False

#     for char in password:
#         if char.isupper():
#             has_uppercase = True
#         elif char.islower():
#             has_lowercase = True
#         elif char.isdigit():
#             has_digit = True

#     # Check for spaces
#     if ' ' in password:
#         return False

#     # Return True only if all checks pass
#     return has_uppercase and has_lowercase and has_digit

# # Test cases
# print(validate_password("Password123"))    # Should print True
# print(validate_password("abc123"))          # Should print False (no uppercase letter)
# print(validate_password("Password 123"))    # Should print False (contains a space)
# print(validate_password("password123"))     # Should print False (no uppercase letter)





# print (2+2)

# print("My mother is the best cook in the world")
 
# print("'What a cruel world we live in")

# name = input ('What is your name Eric')


# print ("Hello ", name)

# num1, num2 = input("Enter 2 numbers ").split()

# num1 =int(num1)
# num2 =int(num2)

# sum = num1 + num2
# difference = num1 - num2
# divide = num1 / num2
# multiply = num1 * num2

# print ("{}+{}={}".format (num1, num2, sum))
# print ("{}-{}={}".format  (num1, num2, difference))
# print ("{}/{}={}".format (num1, num2 ,divide))
# print ("{}*{}={}".format (num1, num2, multiply))

# miles = input ("enter miles ")
# miles = int(miles)
# kilometers = miles * 1.60934

# print (miles, "equals", kilometers)

# def my_function():
#     print("In my function")

# my_function

# def my_function(counter=89):
#     print("Counter: {}".format(counter))
# my_function(12)
# def my_function():
#     print("In my function")
# my_function()

# def my_function(counter=89):
#      print("Counter: {}".format(counter))

# my_function()

# def my_function(counter):
#      print("Counter: {}".format(counter))

# my_function(12)

# def my_function(counter=89):
#    return counter + 1
# print(my_function())


# def add(a, b):
#     return a + b

# if __name__ == "__main__":
#     # Your code here for direct execution
#     a = 5
#     b = 9
#     result = add(a, b)
# print(f"{a} + {b} = {result}")

# for a in range(5, 11):
#     print ("a = ", a)

for i in range (21):
    if (i % 2) ! == 0:
        print ("i = ", i)