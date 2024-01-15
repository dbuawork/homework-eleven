#### Підрахунок кількості слів у текстовому файлі:

with open('text.txt', 'r') as file:
    content = file.read()

words = content.split()
word_count = len(words)

print(f"Кількість слів у текстовому файлі: {word_count}")


