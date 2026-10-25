# replace.py

text = input()

count = text.count(':')
new_text = text.replace(':', '-')

print(f"Количество замен: {count}")
print(new_text)