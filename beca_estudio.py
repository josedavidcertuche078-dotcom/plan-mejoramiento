promedio = float(input("Promedio: "))
matricula = input("Tiene matricula activa? (si/no): ").lower() == "si"

if promedio >= 4.5 and matricula:
    print("Cumple los requisitos preliminares")
else:
    print("No cumple los requisitos preliminares")
