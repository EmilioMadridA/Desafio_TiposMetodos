from personaje import Personaje
from random import uniform

def iniciar_juego():
    print("¡Bienvenido a Gran Fantasía!")
    nombre = input("Por favor indique nombre de su personaje: \n")
    jugador = Personaje(nombre)
    orco = Personaje("Orco")
    
    print(jugador.nombre)
    print(jugador.nivel)
    print(jugador.experiencia)


iniciar_juego()