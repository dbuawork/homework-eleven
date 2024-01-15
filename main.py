#### Підрахунок кількості слів у текстовому файлі:

with open('text.txt', 'r') as file:
    content = file.read()

words = content.split()
word_count = len(words)

print(f"Кількість слів у текстовому файлі: {word_count}")

###################### Перевірка тексту на неприпустимі слова та їх заміна:
def process_text(text, forbidden_word):
    words = text.split()
    count = 0

    for i in range(len(words)):
        if forbidden_word.lower() == words[i].lower():
            words[i] = '*' * len(forbidden_word)
            count += 1

    return ' '.join(words), count


text = """In March, when the trees begin to bloom, spring comes. 
The last Sunday of March, they celebrate Mother’s Day. C
hildren prepare cards, poems and songs for their mums. 
Another important spring holiday is Easter. 
On 1st of May they don’t work, because it’s a Labor Day. 
They decorate their houses and the traditional maypole with garlands and ribbons. 
Then they dance around the maypole."""

forbidden_word = 'March,'

processed_text, replacements_count = process_text(text, forbidden_word)

print("Результат:")
print(processed_text)
print(f"\nСтатистика: {replacements_count} заміни(-в) слова '{forbidden_word}'.")