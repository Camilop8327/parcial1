class Transporte:

    def __init__(self,color,velocidad):

        self.color=color
        self.velocidad=velocidad

moto=Transporte("Color: Negro", "Velocidad:0")

print(type(moto))

print(moto.color, moto.velocidad)