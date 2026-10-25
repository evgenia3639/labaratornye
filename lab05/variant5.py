# variant5.py

text = input()


clean_words = []
for word in text.split():
    w = word.strip(".,!?;:").lower()
    if w:
        clean_words.append(w)


result = [w for w in clean_words if w.endswith("а")]

if not result:
    print("Нет совпадений")
    print(0)
else:
    for w in result:
        print(w)
    print(len(result))