# transform.py

data = input().split()
nums = [int(x) for x in data]

new_nums = [abs(x) for x in nums]

print(nums)
print(new_nums)