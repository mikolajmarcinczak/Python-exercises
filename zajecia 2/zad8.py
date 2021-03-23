employee = {
    'imie':'Julia',
    'nazwisko':'Nowak',
    'miasto':'Poznań',
    'imionaDzieci':['Anna', 'Paweł', 'Dariusz']
}

print(employee)
print(type(employee))

print(f'Imiona dzieci: {employee["imionaDzieci"]}')
print(f'Imionę drugiego dziecka: {employee["imionaDzieci"][1]}')

employee['telefon'] = '1233454567654'
employee['wiek'] = 35

print(employee)

del employee['imionaDzieci']

print(f'Klucze w słowniku: {", ".join(employee.keys())}')