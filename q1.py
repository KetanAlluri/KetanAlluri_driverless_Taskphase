
n = int(input("Enter the number of strings: "))
string_list = []
print(f"Enter {n} strings:")
for _ in range(n):
    string_list.append(input())
char_counts = {}
for string in string_list:
    for char in string.lower():
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
print("Alphabet counts:",sorted(char_counts.items()))
