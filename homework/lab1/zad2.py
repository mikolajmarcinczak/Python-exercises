word = ""
while True:
    if len(word) >= 8 and word.isalpha():
        rev = word[1:-1][::-1] #jestem w ciężkim szoku, że można tu robić takie numery, naprawdę przepraszam ale muszę to zostawić
        print("Wynik: " + word[:3] + word[-2] + word[-4:] + rev)
        break
    else:
        word = input("Napisz jakieś słowo: ")
