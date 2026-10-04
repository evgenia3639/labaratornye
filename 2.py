#time_parts.py

total_seconds = int(input())

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{hours} ч {minutes} мин {seconds} с")

#purchase.py

price = int(input())
count = int(input())
paid = int(input())
cost = price * count
change = paid - cost

print(f"стоимость {cost}, сдача {change}")

#Предскажите результат
#2 + 3 * 4 = 14
#(2 + 3) * 4 = 20
#17 // 5 = 3
#17 % 5 = 2
#-7 // 2 = -4

print(2 + 3 * 4)      # 14
print((2 + 3) * 4)    # 20
print(17 // 5)        # 3
print(17 % 5)         # 2
print(-7 // 2)        # -4


#variant5.py
total_V = int(input())
vmestit = int(input())

full_count_ed = total_V // vmestit
ost = total_V % vmestit
min_ed = (total_V + vmestit - 1) // vmestit

print(full_count_ed, ost, min_ed)