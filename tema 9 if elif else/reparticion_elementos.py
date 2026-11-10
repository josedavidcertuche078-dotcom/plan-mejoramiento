elementos = int(input("Elementos: "))
personas = int(input("Personas: "))
por_persona = elementos // personas
sobran = elementos % personas

print("Por persona:", por_persona)
print("Sobran:", sobran)
