valor = float(input("Valor de la compra: "))

if valor >= 100000:
    envio = 0
else:
    envio = 8000

print("Costo del envio:", envio)
