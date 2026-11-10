edad = int(input("Edad: "))

if edad < 12:
    print("Tarifa infantil")
elif edad < 18:
    print("Tarifa juvenil")
else:
    print("Tarifa general")
