import psycopg2
import settings
from domain import *

# def get_all():
#     products = []
#     p1 = Product(1, "Bulbulator", 1000, "robi bul bul", 10)
#     products.append(p1)
#     p2 = Product(2, "Przyczłap do bulbulatora", 200, "Taki wihajster co ten no wiadomo", 2)
#     products.append(p2)
#     p3 = Product(3, "Dzyndzel do przyczłapa", 50, "Taki teges z tym że ten", 0)
#     products.append(p3)
#     return products

def get_all():
    products = []
    with psycopg2.connect(host=settings.host,database=settings.database,port=settings.port, user=settings.user,password=settings.password) as connection:
        cursor=connection.cursor()
        cursor.execute("select * from produkty")
        for w in cursor:
            product=Product(w[0],w[1],w[2],w[3],w[4])
            products.append(product)
    return products

# def get_one(id):
#     product=Product(id,"Przykładowy obiekt",50,'opis przykładowego obiektu który może być bardzo długi',3)
#     return product

def get_one(id):
    with psycopg2.connect(host=settings.host, database=settings.database, port=settings.port, user=settings.user, password=settings.password) as connection:
        cursor = connection.cursor()
        cursor.execute(f"select * from produkty where id_produktu={id}")
        w=cursor.fetchone()
        product = Product(w[0], w[1], w[2], w[3], w[4])
        return product