from models import Products
from orm import session


class UserMethods:

    @classmethod
    def create_product(cls):
        name = input("Ingrese el nombre del producto: ")
        price  = int(input("Ingrese el precio: "))
        product = Products(name, price)
        session.add(product)
        session.commit()
    
    @classmethod
    def get_product(cls):
        ob = session.query(Products).get(1)
        ob_all = session.query(Products).all()
        first = session.query(Products).first()
        print(ob)


    @classmethod
    def delete_user(cls):
        ob = session.query(Products).get(2)
        session.delete(ob)
        session.commit()
    
    @classmethod
    def update_user(cls):
        ob = session.query(Products).get(1)
        ob.nombre = "Cambio!!"
        session.commit()

#UserMethods.create_product()
#UserMethods.get_product()
#UserMethods.delete_user()
UserMethods.update_user()