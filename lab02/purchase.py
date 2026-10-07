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