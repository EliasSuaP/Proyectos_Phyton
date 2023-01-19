import random


def jugar():
    usuario = input("Escoge una opción 'pi' para piedra, 'pa' para papel y 'ti' para tijera.\n").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        return(f"¡Empate! Por que {usuario} x {computadora} son iguales!")

    if gano_el_jugador(usuario, computadora):
        return (f"¡Ganaste! Por que {usuario} gana a {computadora} !")

    return(f"¡Perdiste! Por que {computadora} gana a {usuario} !")


def gano_el_jugador(jugador, oponente):
    #Retorna true si gana el jugador
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar())    

#Agregar un mensaje donde se comparen los valores de usuario y computadora

#realizar función para mostrar comparación completa de la selección
pi = "piedra" 
pa = "papel"
ti = "tijera"