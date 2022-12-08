import psycopg2
import settings
from domain import *
#
# def get_all():
#     employees = []
#     e1 = Employee(1, "Ferdynand", "Kiepski", 6000,"jakiś długi komentarz do pracownika. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. ")
#     employees.append(e1)
#     e2 = Employee(2, "Młody", "Kiepski", 3000,"jakiś długi komentarz do pracownika. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. ")
#     employees.append(e2)
#     e3 = Employee(3, "Babka", "Kiepska", 8000, "jakiś długi komentarz do pracownika. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. ")
#     employees.append(e3)
#     return employees



def get_all():
    employees = []
    with psycopg2.connect(host=settings.host,database=settings.database,port=settings.port, user=settings.user,password=settings.password) as connection:
        cursor=connection.cursor()
        cursor.execute("select * from pracownicy")
        for w in cursor:
            employee=Employee(w[0],w[1],w[2],w[3],w[4])
            employees.append(employee)
    return employees


# def get_one(id):
#     employee = Employee(id, "Andrzej", "Kowalski", 100000, "Dobry pracownik (pije i nie kabluje)")
#     return employee

def get_one(id):
    with psycopg2.connect(host=settings.host, database=settings.database, port=settings.port, user=settings.user,  password=settings.password) as connection:
        cursor = connection.cursor()
        cursor.execute(f"select * from pracownicy where id_pracownika={id}")
        w=cursor.fetchone()
        employee = Employee(w[0], w[1], w[2], w[3], w[4])
        return employee

def save(employee):
    sql=f"insert into pracownicy(imie,nazwisko,zarobki,komentarz) values ('{employee.first_name}','{employee.last_name}',{employee.salary},'{employee.comment}')"
    print(sql)
    with psycopg2.connect(host=settings.host, database=settings.database, port=settings.port, user=settings.user,  password=settings.password) as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()


def delete(id):
    sql=f"delete from pracownicy where id_pracownika={id}"
    with psycopg2.connect(host=settings.host, database=settings.database, port=settings.port, user=settings.user,password=settings.password) as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()