
input_ = input("Введите функцию: ").replace(' ', '')

# def math(op):
#     if '+' in input_:
#         return "+"
#     if '-' in input_:
#         return "-"
#     if '*' in input_:
#         return '*'
#     if '/' in input_:
#         return "/"


for element in input_:
    if element == "+":
        op = "+"
        break
    if element == "-":
        op = "-"
        break
    if element == "*":
        op = "*"
        break
    if element == "/":
        op = "/"
        break
else:
    print("net znaka")
print(op)


def operation(a, b, op):
    try:
        if op == '+':
            return float(a) + float(b)
        elif op == '-':
            return float(a) - float(b)
        elif op == '*':
            return float(a) * float(b)
        elif op == '/':
            return float(a) / float(b)
    except ValueError as e:
        print(e)


i = input_.index(op)
print('i is :', i)
a = input_[:i]
print('A is :', a)
b = input_[i+1:]
print('B is :', b)
print(operation(a, b, op))
