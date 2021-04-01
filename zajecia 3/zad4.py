def Palindrome(word):
    return word == word[::-1]
print(f'Słowo {"nie " if not Palindrome(input("Wprowadź słowo: ")) else ""}jest palindromem.')