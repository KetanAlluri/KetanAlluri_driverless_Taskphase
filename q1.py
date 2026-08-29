from collections import Counter

n = int(input("Enter n: "))

letter_count = Counter()

for _ in range(n):
    text = input("Enter a string: ")
    letter_count.update(text.lower())

for letter, count in sorted(letter_count.items()):
    if letter.isalpha():
        print(letter,":", count)