# # def validate_password(password):
# #     # Check the length of the password
# #     if len(password) < 8:
# #         return False

# #     # Check for at least one uppercase letter, one lowercase letter, and one digit
# #     has_uppercase = False
# #     has_lowercase = False
# #     has_digit = False

# #     for char in password:
# #         if char.isupper():
# #             has_uppercase = True
# #         elif char.islower():
# #             has_lowercase = True
# #         elif char.isdigit():
# #             has_digit = True

# #     # Check for spaces
# #     if ' ' in password:
# #         return False

# #     # Return True only if all checks pass
# #     return has_uppercase and has_lowercase and has_digit

# # # Test cases
# # print(validate_password("Password123"))    # Should print True
# # print(validate_password("abc123"))          # Should print False (no uppercase letter)
# # print(validate_password("Password 123"))    # Should print False (contains a space)
# # print(validate_password("password123"))     # Should print False (no uppercase letter)





# # print (2+2)

# # print("My mother is the best cook in the world")
 
# # print("'What a cruel world we live in")

# # name = input ('What is your name Eric')


# # print ("Hello ", name)

# # num1, num2 = input("Enter 2 numbers ").split()

# # num1 =int(num1)
# # num2 =int(num2)

# # sum = num1 + num2
# # difference = num1 - num2
# # divide = num1 / num2
# # multiply = num1 * num2

# # print ("{}+{}={}".format (num1, num2, sum))
# # print ("{}-{}={}".format  (num1, num2, difference))
# # print ("{}/{}={}".format (num1, num2 ,divide))
# # print ("{}*{}={}".format (num1, num2, multiply))

# # miles = input ("enter miles ")
# # miles = int(miles)
# # kilometers = miles * 1.60934

# # print (miles, "equals", kilometers)

# # def my_function():
# #     print("In my function")

# # my_function

# # def my_function(counter=89):
# #     print("Counter: {}".format(counter))
# # my_function(12)
# # def my_function():
# #     print("In my function")
# # my_function()

# # def my_function(counter=89):
# #      print("Counter: {}".format(counter))

# # my_function()

# # def my_function(counter):
# #      print("Counter: {}".format(counter))

# # my_function(12)

# # def my_function(counter=89):
# #    return counter + 1
# # print(my_function())


# # def add(a, b):
# #     return a + b

# # if __name__ == "__main__":
# #     # Your code here for direct execution
# #     a = 5
# #     b = 9
# #     result = add(a, b)
# # print(f"{a} + {b} = {result}")


# #!/usr/bin/python3
# # from add_0 import add as add_0

# # a = 1
# # b = 2
# # result = add_0(a, b)
# # print("{} + {} = {}".format(a, b, result))



# # if __name__ == "__main__":
# #     from add_0 import add
# #     a = 1
# #     b = 2
# #     print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))


# # """Pullingthe total of 1 and 2"""

# # if __name__ == "__main__":
# #     from add_0 import add
# #     a = 1
# #     b = 2
# #     print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

# # i = "Chicago"
# # a = i.replace("c", "").replace("C", "")
# # print(a)

# # i = "Chicago"
# # a = ''.join(c for c in i if c not in {'C', 'c'})
# # print(a)


# # def print_matrix_integer(matrix=[[]]):
# #     for row in matrix:
# #         for i, num in enumerate(row):
# #             if i == len(row) - 1:
# #                 print("{:d}".format(num), end="")
# #             else:
# #                 print("{:d} ".format(num), end="")
# #         print()

# # # Example usage:
# # if __name__ == "__main__":
# #     matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# #     # print("--")
# #     print_matrix_integer ("matrix", str.format("$"))


# # def print_matrix_integer(matrix=[[]]):
# #     for row in matrix:
# #         for i, num in enumerate(row):
# #             if i == len(row) - 1:
# #                 print("{:d}".format(num), end="")
# #             else:
# #                 print("{:d} ".format(num), end="")
# #         print("".format(row[-1]))

# # # Example usage:
# # if __name__ == "__main__":
# #     matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# #     print_matrix_integer(matrix)


# # letters = ['a', 'b', 'c', 'd'], 
# # len(letters)

# # empty = ()
# # singleton = 'hello',    # <-- note trailing comma
# # print (len(singleton))


# # def multiple_returns(sentence):
# #     # Check if the sentence is empty
# #     if not sentence:
# #         return None
    
# #     # Return a tuple with the length and the first character
# #     return len(sentence), sentence[0]
    
# # # Example usage:
# # result = multiple_returns("At Holberton school, I learnt C!")
# # # print("Lenght:", result, )  
# # # lenght = len ()
# # # first = sentence [0]
# # print("Length: {} - First character: {}".format(result[0], result[1]) )

# # empty_result = multiple_returns("")
# # print(empty_result)  

# # def multiple_returns(sentence):
# #     # Check if the sentence is empty
# #     if not sentence:
# #         return (0, None)
    
# #     # Return a tuple with the length and the first character
# #     return (len(sentence), sentence[0])

# # # Example usage:
# # result = multiple_returns("At Holberton school, I learnt C!")
# # print("Length: {} - First character: {}".format(result[0], result[1]))

# # empty_result = multiple_returns("")
# # print("Length: {} - First character: {}".format(empty_result[0], empty_result[1]))

# def multiple_returns(sentence):
#     # Check if the sentence is empty
#     if not sentence:
#         return (0, None)
    
#     # Return a tuple with the length and the first character
#     return (len(sentence), sentence[0])
#     else

# # if __name__ == "__main__":
# #     # Example usage:
# #     result = multiple_returns("Hello, World!")
# #     print("Length: {} - First character: {}".format(result[0], result[1]))

# #     empty_result = multiple_returns("")
# #     if empty_result[0] == 0:
# #         print("Length: {} - First character: {}".format(empty_result[0], "None"))
# #     else:
# #         print("Unexpected output for an empty string.")


# a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
# print(a.get('friends')[-1].get("name"))

# a= set("sdfgdghffgh")
# b= set("dfghtdwxcdvy")
# print (b-a)

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = [row[:] for row in matrix]

    # Iterate over each element in the matrix and square the value
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix

# Example usage:
if __name__ == "__main__":
    # Sample matrix
    input_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Compute the square matrix
    result_matrix = square_matrix_simple(input_matrix)

    # Print the result
    for row in result_matrix:
        print(row)
