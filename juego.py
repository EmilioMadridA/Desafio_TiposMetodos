from personaje import Personaje
from random import uniform

def iniciar_juego():
    """ Inicia y ejecuta el flujo principal del juego 'Gran Fantasía'.
    """
    # Saludo inicial y creación del personaje del jugador.
    print("¡Bienvenido a Gran Fantasía!")
    nombre = input("Por favor indique nombre de su personaje: \n")
    jugador = Personaje(nombre)
    orco = Personaje("Orco")
    
    # Print para mostrar el estado inicial del personaje del jugador.
    print(jugador)

    # Ciclo while principal del juego.
    while True:
        print("\n¡Oh no!, ¡Ha aparecido un Orco!")

        # Calculo de la probabilidad de ganar contra el orco.
        probabilidad = jugador.probabilidad_vs(orco)

        # Print con la posibilidad de victoria y resultados.
        print(f"\nCon tu nivel actual, tienes {probabilidad}% de probabilidades de ganarle al Orco.\n")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50. \n")
        
        # Solicitud de accion al usuario
        accion = input("¿Qué deseas hacer? \n1. Atacar \n2. Huir \n")
        
        # Validacion de accion
        if accion == "1":
            resultado = "Gana" if uniform(0, 1) <= probabilidad / 100 else "Pierde"
            if resultado == "Gana":
                print("\n¡Le has ganado al orco, felicidades! \n")
                jugador.asignar_exp(50)
                orco.asignar_exp(-30)
            else:
                print("\n¡Oh no! ¡El orco te ha ganado! \n")
                jugador.asignar_exp(-30)
                orco.asignar_exp(50)
                
            print(jugador)
            print(orco)
        elif accion == "2":
            print("\n¡Has huido! El orco ha quedado atrás.")
            break

iniciar_juego() # Llamada a la funcion de inicio del juego.