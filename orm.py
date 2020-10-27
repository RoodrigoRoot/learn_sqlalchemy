#Primero crearemos uyn engine
#Este es el que nos va a permitir poder conectar a la base de datos
#Básicamente hablamos de la conexión y que dialecto va a utilizar
#solo especifianco a quien nos conectaremos, el engine sabrá que dialecto utilizar

#from sqlalchemy import create_engine
#engine = create_engine('sqlite:///productos.sqlite')


#Después procedemos con crear una sesión
#Esto para que nosotros podamos hacer las transacciones que necesitemos
#Insertar, Actualizar, Consultar o Eliminar
#Haciendolo de una manera atomica (Todo o Nada)

from sqlalchemy.orm import sessionmaker#Con el crearemos una sesión
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://rod:forever11@localhost/alchemy')
Session = sessionmaker(bind=engine)#asociamos nuestor engine
session = Session()#y ahora tenemos un objeto para las sesiones
Base = declarative_base() #Esto nos permitirá el poder mapear de clases a tabla y vicecersa
