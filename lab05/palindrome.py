#palindrome.py

text = input()

clean = text.replace(" ", "").lower() #заглавные в строчные

if not clean:
    print("Нет текста")
elif clean == clean[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")