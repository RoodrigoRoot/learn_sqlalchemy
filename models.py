#Modelos son clases para representar a las tablas que vamos a tener en nuestr DB
#Para crear nuestros modelos debemos importar los tipos de datos que usaremos

import orm
from sqlalchemy import String, Float, Integer, Column

class Products(orm.Base):

    __tablename__ = "Productos"

    id = Column(Integer, primary_key=True) #Aquí creamos un una columna llamada id de tipo
                                           #Integer y que será nuestra llave primaria
        
    nombre = Column(String, nullable=False) #Podemos indicar si los valores pueden o no aceptar valores nulos
    precio = Column(Float)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def __repr__(self):
        return f'Producto({self.nombre}, {self.precio})'
        
    def __str__(self):
        return self.nombre