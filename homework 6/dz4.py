import json
import csv
with open('test.json') as file:
    x= json.load(file)
numbers = [123, 234, 333, 444, 555, 666]
print(x)
for index, key in enumerate(x):
        x[key].append(numbers[index])
#for i in (x, numbers):
#        x[i].append(numbers(i))
print(x)

with open('2.csv', 'w+') as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(('id', 'name', 'age', 'phone'))
    for key, value in x.items():
        writer.writerow([key, *value])
        pass