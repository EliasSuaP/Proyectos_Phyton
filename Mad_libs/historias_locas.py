# concatenar cadenas de caracteres
# Supongamos que queremos crear una cadena que diga:
# Aprende a programar con ____________-


adj = input("Ingrese un adjetivo: ")
verbo1 = input("Ingrese un verbo: ")
verbo2 = input("Ingrese otro verbo: ")
sustantivo_plural = input("Ingrese un sustantivo en plural: ")

madlib = f"¡Programar es tan {adj}! Siempre me emociona por que me encanta {verbo1} problemas. ¡Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!"

print(madlib)