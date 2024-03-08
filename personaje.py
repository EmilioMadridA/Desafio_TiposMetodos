class Personaje():
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def __str__(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"

    def asignar_exp(self, experiencia):
        temp_exp = self.experiencia + experiencia
        while temp_exp >= 100:
            self.nivel += 1
            temp_exp -= 100
        while temp_exp < 0 and self.nivel > 1:
            self.nivel -= 1
            temp_exp += 100
        self.experiencia = temp_exp if temp_exp >= 0 else 0

    def __lt__(self, otro):
        return self.nivel < otro.nivel
    
    def __gt__(self, otro):
        return self.nivel > otro.nivel
    
    def __eq__(self, otro):
        return self.nivel == otro.nivel

    def probabilidad_vs(self, otro):
        if self > otro:
            return 66.0
        elif self < otro:
            return 33.0
        else:
            return 50.0