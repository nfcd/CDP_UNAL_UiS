import numpy as np

class Circulo:
    """
    Una clase que implementa un círculo
    """
    # La inicializacion requiere el centro [x, y]
    # y radio del circulo    
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    
    # otros atributos derivados del círculo
    
    # circunferencia
    def circunferencia(self):
        return 2 * np.pi * self.radio
    
    # área
    def area(self):
        return np.pi * self.radio ** 2
    
    # las coordenadas x, y que definen el círculo
    def coordenadas(self):
        theta = np.arange(0,360) * np.pi / 180
        x = self.radio * np.cos(theta) + self.centro[0]
        y = self.radio * np.sin(theta) + self.centro[1]
        return x, y
    
    # métodos de la clase
    
    # desplaze el centro del círculo en x
    def mueva_en_x(self, x_valor):
        self.centro[0] += x_valor
    
    # desplaze el centro del círculo en y
    def mueva_en_y(self, y_valor):
        self.centro[1] += y_valor