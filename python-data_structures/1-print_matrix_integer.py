def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(num), end="")
            else:
                print("{:d} ".format(num), end="")
        print("",str.format("$"))

# if __name__ == "__main__":
#     matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
#     print_matrix_integer (matrix)