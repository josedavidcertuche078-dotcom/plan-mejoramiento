inscrita = input("Esta inscrita? (si/no): ").lower() == "si"
identificacion = input("Presento identificacion? (si/no): ").lower() == "si"

if inscrita and identificacion:
    print("Cumple ambos requisitos")
else:
    print("No cumple ambos requisitos")
