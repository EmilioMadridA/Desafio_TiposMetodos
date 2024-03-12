class Personaje():
    def __init__(self, nombre):
        """ Metodo que inicializa una nueva instancia de la clase con valores predeterminados.

        Args:
            nombre (str): Nombre ingresado por el usuario, se usa para generar la instancia de clase.
        """
        self.nombre = nombre
        self.nivel = 1 # Establece el nivel inicial del objeto en 1.
        self.experiencia = 0 # Inicia la experiencia del objeto en 0.

    def __str__(self):
        """ Este método especial es invocado por la función integrada str() y por la función print()
        para obtener una representación legible de la instancia. Proporciona una manera conveniente
        de mostrar el estado actual del objeto, incluyendo su nombre, nivel y experiencia.

        Returns:
            str: Descripcion del objeto de la instancia invocada.
        """
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"

    def asignar_exp(self, experiencia):
        """ Metodo que asigna experiencia al objeto y ajusta su nivel según la cantidad de experiencia proporcionada.

        Args:
            experiencia (int): La cantidad de experiencia a asignar al objeto. Puede ser positiva para aumentar la 
            experiencia o negativa para reducirla.
        """
        temp_exp = self.experiencia + experiencia # Experiencia temporal que se obtiene al sumar la actual con la nueva asignada
        # Ciclo while de validación de experiencia asignada, y su correcto tratamiento dependiente del valor de la misma.
        while temp_exp >= 100:
            self.nivel += 1
            temp_exp -= 100
        while temp_exp < 0 and self.nivel > 1:
            self.nivel -= 1
            temp_exp += 100
        self.experiencia = temp_exp if temp_exp >= 0 else 0

    def __lt__(self, otro):
        """ Este metodo comprueba si el nivel de esta instancia es menor que el de otra.

        Args:
            otro (objetc): Otra instancia de la misma clase contra la cual se compara.

        Returns:
            bool: Retorna True si el nivel de esta instancia es menor que el de 'otro', False de lo contrario.
        """
        return self.nivel < otro.nivel
    
    def __gt__(self, otro):
        """ Este metodo comprueba si el nivel de esta instancia es mayor que el de otra.

        Args:
            otro (objetc): Otra instancia de la misma clase contra la cual se compara.

        Returns:
            bool: Retorna True si el nivel de esta instancia es mayor que el de 'otro', False de lo contrario.
        """
        return self.nivel > otro.nivel
    
    def __eq__(self, otro):
        """ Este metodo comprueba si el nivel de esta instancia es igual al de otra.

        Args:
            otro (objetc): Otra instancia de la misma clase contra la cual se compara.

        Returns:
            bool: Retorna True si el nivel de esta instancia es igual que el de 'otro', False de lo contrario.
        """
        return self.nivel == otro.nivel

    def probabilidad_vs(self, otro):
        """ Este metodo calcula la probabilidad de que esta instancia gane contra otra en base a su nivel.

        Args:
            otro (objetc): Otra instancia de la misma clase contra la cual se compara.

        Returns:
            float: Retorna la probabilidad de ganar, en formato de porcentaje.
        """
        if self > otro:
            return 66.0
        elif self < otro:
            return 33.0
        else:
            return 50.0