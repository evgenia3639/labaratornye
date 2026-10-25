# statistics.py

data = input().split()

if not data:
    print("Нет данных")
else:
    nums = [int(x) for x in data]

    count = len(nums)
    total = sum(nums)
    mini = min(nums)
    maxi = max(nums)
    sred = total / count

    print(count)
    print(total)
    print(mini)
    print(maxi)
    print(f"{sred:.2f}")


