

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, matricula, modelo):
        self.__matricula = matricula
        self.__modelo = modelo

    def get_matricula(self):
        return self.__matricula

    def get_modelo(self):
        return self.__modelo

    @abstractmethod
    def imprimir(self):
        pass

class VehiculoTerrestre(Vehiculo):
    def __init__(self, matricula, modelo, num_ruedas):
        super().__init__(matricula, modelo)
        self.__num_ruedas = num_ruedas

    def get_num_ruedas(self):
        return self.__num_ruedas

    def imprimir(self):
        pass

class Coche(VehiculoTerrestre):
    def __init__(self, matricula, modelo, num_ruedas, aire_acondicionado):
        super().__init__(matricula, modelo, num_ruedas)
        self.__aire_acondicionado = aire_acondicionado

    def get_aire_acondicionado(self):
        return self.__aire_acondicionado

    def imprimir(self):
        print(f"Matrícula: {self.get_matricula()}, Modelo: {self.get_modelo()}, Número de ruedas: {self.get_num_ruedas()}, Aire acondicionado: {self.__aire_acondicionado}")

class Moto(VehiculoTerrestre):
    def __init__(self, matricula, modelo, num_ruedas, color):
        super().__init__(matricula, modelo, num_ruedas)
        self.__color = color

    def get_color(self):
        return self.__color

    def imprimir(self):
        print(f"Matrícula: {self.get_matricula()}, Modelo: {self.get_modelo()}, Número de ruedas: {self.get_num_ruedas()}, Color: {self.__color}")

class VehiculoAcuatico(Vehiculo):
    def __init__(self, matricula, modelo, eslora):
        super().__init__(matricula, modelo)
        self.__eslora = eslora

    def get_eslora(self):
        return self.__eslora

    @abstractmethod
    def imprimir(self):
        pass

class Barco(VehiculoAcuatico):
    def __init__(self, matricula, modelo, eslora, motor):
        super().__init__(matricula, modelo, eslora)
        self.__motor = motor

    def get_motor(self):
        return self.__motor

    def imprimir(self):
        print(f"Matrícula: {self.get_matricula()}, Modelo: {self.get_modelo()}, Eslora: {self.get_eslora()}, Motor: {self.__motor}")

class Submarino(VehiculoAcuatico):
    def __init__(self, matricula, modelo, eslora, profundidad_maxima):
        super().__init__(matricula, modelo, eslora)
        self.__profundidad_maxima = profundidad_maxima

    def get_profundidad_maxima(self):
        return self.__profundidad_maxima

    def imprimir(self):
        print(f"Matrícula: {self.get_matricula()}, Modelo: {self.get_modelo()}, Eslora: {self.get_eslora()}, Profundidad máxima: {self.__profundidad_maxima}")

class VehiculoAereo(Vehiculo):
    def __init__(self, matricula, modelo, num_asientos):
        super().__init__(matricula, modelo)
        self.__num_asientos = num_asientos

    def get_num_asientos(self):
        return self.__num_asientos

    @abstractmethod
    def imprimir(self):
        pass

class Avion(VehiculoAereo):
    def __init__(self, matricula, modelo, num_asientos, tiempo_max_vuelo):
        super().__init__(matricula, modelo, num_asientos)
        self.__tiempo_max_vuelo = tiempo_max_vuelo

    def get_tiempo_max_vuelo(self):
        return self.__tiempo_max_vuelo

    def imprimir(self):
        print(f"Matrícula: {self.get_matricula()}, Modelo: {self.get_modelo()}, Número de asientos: {self.get_num_asientos()}, Tiempo máximo de vuelo: {self.__tiempo_max_vuelo}")

class Helicoptero(VehiculoAereo):
    def __init__(self, matricula, modelo, num_asientos, num_helices):
        super().__init__(matricula, modelo, num_asientos)
        self.__num_helices = num_helices

    def get_num_helices(self):
        return self.__num_helices

    def imprimir(self):
        print(f"Matrícula: {self.get_matricula()}, Modelo: {self.get_modelo()}, Número de asientos: {self.get_num_asientos()}, Número de hélices: {self.__num_helices}")

class Programa:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def imprimir_vehiculos(self):
        for vehiculo in self.vehiculos:
            vehiculo.imprimir()