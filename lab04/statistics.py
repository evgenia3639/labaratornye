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