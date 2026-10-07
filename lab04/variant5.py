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