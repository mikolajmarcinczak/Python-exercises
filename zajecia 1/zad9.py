zdanie = input("Wprowadź swoje zdanie: ")
b = ""
list = "aeiouy"

for n in zdanie:
    if n in list:
        b += n.upper()
    else: 
        b += n
print(b)