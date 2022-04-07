class Racional():
    def __init__(self, numerador, denominador):
        self.numerador = int(numerador)
        if denominador == 0:
            raise Exception("El denominador no puede ser 0")
        self.denominador = int(denominador)

    def __str__(self):
        return str(self.numerador) + "/" + str(self.denominador)

    def equivalente(self, otra: 'Racional') -> bool:
        return self.denominador == otra.denominador and self.numerador == otra.numerador


    def maximo_comun_divisor(self, a, b):
        temporal = 0
        while b != 0:
            temporal = b
            b = a % b
            a = temporal
        return a

    def minimo_comun_multiplo(self, a, b):
        return (a * b) / self.maximo_comun_divisor(a, b)

    def suma(self, otra: 'Racional') -> 'Racional':
        mcm = self.minimo_comun_multiplo(self.denominador, otra.denominador)
        diferencia_self = mcm/self.denominador
        diferencia_otra = mcm/otra.denominador
        numerador_resultado = (diferencia_self*self.numerador) + \
            (diferencia_otra*otra.numerador)
        return Racional(numerador_resultado, mcm)

    def resta(self, otra: 'Racional') -> 'Racional':
        mcm = self.minimo_comun_multiplo(self.denominador, otra.denominador)
        diferencia_self = mcm/self.denominador
        diferencia_otra = mcm/otra.denominador
        numerador_resultado = (diferencia_self*self.numerador) - \
            (diferencia_otra*otra.numerador)
        return Racional(numerador_resultado, mcm)

    def producto(self, otra: 'Racional') -> 'Racional':
        return Racional(self.numerador*otra.numerador, self.denominador*otra.denominador)

    def cociente(self, otra: 'Racional') -> 'Racional':
        return Racional(self.numerador*otra.denominador, self.denominador*otra.numerador)

    def inversa(self) -> 'Racional':
        return Racional(self.denominador, self.numerador)

    def potencia(self, exponente) -> 'Racional':
        return Racional(self.numerador ** exponente, self.denominador ** exponente)

    def simplifica(self) -> 'Racional':
        mcd = self.maximo_comun_divisor(self.numerador, self.denominador)
        return Racional(self.numerador / mcd, self.denominador / mcd)
