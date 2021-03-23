u_str = input("Wprowadź ciąg znaków: ")
arr = []
arr = u_str.split(',')

i = 0
for item in arr:
    arr[i] = str(i) + item
    i += 1
n_str = ""
for item in arr:
    n_str += item
print("Twój ciąg zamienił się w {}".format(n_str))