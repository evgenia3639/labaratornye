#range_numbers.py
a = int(input())
b = int(input())

if a < b:
    for i in range(a, b + 1):
        print(i)
elif a > b:
    for i in range(a, b - 1, -1):
        print(i)
else:
    print(a)

#statistics.py
n = int(input())

x = int(input())
total = x
positive_count = 1 if x > 0 else 0
maxi = x

for _ in range(n - 1):
    x = int(input())
    total += x
    if x > 0:
        positive_count += 1
    if x > maxi:
        maxi = x

print(total)
print(positive_count)
print(maxi)

#positive_input.py
count = 0

while True:
    x = int(input())
    if x > 0:
        break
    count += 1

print(x ** 2)
print(count)

#variant.py
n = int(input())

count = 0
summa = 0

for _ in range(n):
    x = int(input())
    if x > 0:
        count += 1
        summa += x

print(count)
print(summa)