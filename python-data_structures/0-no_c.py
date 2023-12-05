i = "Chicago"
a = ''.join(c for c in i if c not in {'C', 'c'})
print(a)