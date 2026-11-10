edad = int(input("Edad: "))
documento = input("Documento vigente (True/False): ") == "True"

puede = edad >= 18 and documento
print("Puede:", puede)
