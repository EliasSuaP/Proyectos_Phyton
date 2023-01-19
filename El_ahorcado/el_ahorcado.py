import random
import string


from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_valida(palabras):
    #seleccionando la palabra al azar
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()    


def ahorcado():

    print("**************************************")
    print(" ¡Bienvenido/a al juego del ahorcado! ")
    print("**************************************")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7 

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        #mostrar estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas 
        else '_' for letra in palabra]
        #mostrar las letras separadas por un espacio
        print(vidas_diccionario_visual[vidas])
        #Mostrar las letras separadas por un espacio
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra mdfk: ").upper()

        #Si la letra escogida por el usuario está en el abecedario y no está en el conjunto de letras que ya se han ingresado, añade la letra al conjunto de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            #Si la letra está en la palabra, quitar la letra del conjunto de letras pendientes por adivinar. Si no está en la palabra, quita una vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        #Si la letra ingresada por el usuario ya fue ingresada.
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por fabor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.") 
    
    #El juego llega a esta línea cuando se adivina todas las letras de la palabra o cuando se agotan las vidas.
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste mdfk. La palabra era: {palabra}")
    else:
        print(f"¡La hiciste hermano! ¡Adivinaste la palabra {palabra}!")


ahorcado()


