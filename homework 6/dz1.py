b = b'r\xc3\xa9sum\xc3\xa9'
print(type(b))
s = b.decode('UTF-8')
print(s)
a=s.encode()
print(a)
a=s.encode(encoding='latin1')
print(a)
