instructora = input("Es instructora (True/False): ") == "True"
autorizacion = input("Tiene autorizacion (True/False): ") == "True"

cumple = instructora or autorizacion
print("Cumple al menos una:", cumple)
