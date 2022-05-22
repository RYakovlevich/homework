a= ("gogog","google","hello","арара")
b= tuple(filter(lambda x: x == x[::-1], a))
print(b)