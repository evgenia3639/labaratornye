# normalize.py

def main():
    text = input()

    words = text.split()
    norma = ' '.join(words)

    print(f"Исходная длина: {len(text)}")
    print(f"Новая длина: {len(norma)}")
    print(norma)
    print(f"Количество слов: {len(words)}")

if __name__ == "__main__":
    main()


