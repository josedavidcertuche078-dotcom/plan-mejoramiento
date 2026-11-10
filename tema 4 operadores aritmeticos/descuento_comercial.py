compra = float(input("Valor de la compra: "))
fidelizacion = input("Pertenece al programa de fidelizacion? (si/no): ").lower() == "si"

if compra > 150000 or fidelizacion:
    print("Aplica promocion")
else:
    print("No aplica promocion")
