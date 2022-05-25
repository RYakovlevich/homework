import json
a= {
    123456: ("name", 30),
    123442: ('name2', 32),
    111112: ('name3', 29),
    111113: ('name4', 28),
    111114: ('name5', 27),
    111115: ('name6', 26),
}
with open("test.json",'w') as file:
    json.dump(a,file)
