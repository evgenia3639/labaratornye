# variant5.py

data = input().split()
nums = [int(x) for x in data]

select = [x for x in nums if x > 0]

print(select)
print(len(select))
print(sum(select))
print(sorted(select))
