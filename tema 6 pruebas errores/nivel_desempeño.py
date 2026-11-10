porcentaje = float(input("Porcentaje de cumplimiento: "))

if porcentaje < 60:
    print("Bajo")
elif porcentaje < 80:
    print("Medio")
elif porcentaje < 95:
    print("Alto")
else:
    print("Excelente")
