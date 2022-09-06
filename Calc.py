s = input("Enter a sign ( + - * / ^) or the root: ")
a = float(input('a = '))
b = float(input('b = '))

if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
elif s == '/':
    print(a / b)
elif s == '^':
    print( a ** b)
elif s == 'root':
    print( a ** 0.5)