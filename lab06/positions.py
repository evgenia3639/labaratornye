# positions.py

data = input().split()

if not data:
    print("Нет данных")
else:
    nums = [int(x) for x in data]

    maxi = max(nums)
    positions = [i for i, v in enumerate(nums) if v == maxi]

    print(positions)