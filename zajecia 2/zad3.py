languages = ["Python", "C#", "JS", "PHP", "Java"]
i = 0

def counter(_list):
    count = 0
    for item in _list:
        if item == "Python":
            count += 1
    return count

for item in languages:
    print("Arg{}: {}".format(i,item))
    i += 1
print("Typ zmiennej - ", type(languages))

print(languages[0])
print(languages[-1])

languages.append("Pascal")
print(languages)

print("Python występuje w liście {} razy".format(counter(languages)))

for i in range(6):
    languages.append("Python")
print("Python występuje w liście {} razy".format(counter(languages)))

arr = ["C#", "Kotlin"]
languages.extend(arr)
print(languages)

print(list(set(languages)))