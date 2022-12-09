from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
import random
from domain import *
import employees_dao as edao
import products_dao as pdao


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://mapet:dupa@localhost/postgres'
db=SQLAlchemy(app)


@app.route('/')
def index():
    return render_template("index.html")#'<h1>Strona główna</h1>'

@app.route('/show_employees')
def show_employees():
    # employees=edao.get_all()
    # for e in employees:
    #     print(e)
    return render_template("show_employees.html",employees=edao.get_all())

@app.route('/employee_details')
def employee_details():
    id=request.args.get('id')
    return render_template("employee_details.html",employee=edao.get_one(id))

@app.route('/add_employee')
def add_employee():
    return render_template("add_employee.html")

@app.route('/add_employee',methods=['POST'])
def add_employee_post():
    #print("request.form=",request.form)
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    salary=request.form['salary']
    comment=request.form['comment']
    employee=Employee(None,first_name,last_name, salary, comment)
    edao.save(employee)
    return redirect('/show_employees')

@app.route('/delete_employee')
def delete_employee():
    id=request.args.get('id')
    return render_template("delete_employee.html",employee=edao.get_one(id))

@app.route('/delete_employee',methods=['POST'])
def delete_employee_post():
    id=request.args.get('id')
    edao.delete(id)
    return redirect("/show_employees")

@app.route('/show_products')
def show_products():
    # products=pdao.get_all()
    # for p in products:
    #     print(p)
    return render_template("show_products.html",products=pdao.get_all())

@app.route('/product_details')
def product_details():
    id=request.args.get('id')
    return render_template("product_details.html",product=pdao.get_one(id))

@app.route('/add_product')
def add_product():
    return render_template("add_product.html")

@app.route('/add_product',methods=['POST'])
def add_product_post():
    name=request.form['name']
    price=request.form['price']
    description=request.form['description']
    stock=request.form['stock']
    product=Product(None,name,price,description,stock)
    pdao.save(product)
    return redirect("/show_products")

@app.route('/delete_product')
def delete_product():
    id=request.args.get('id')
    product=pdao.get_one(id)
    return render_template("delete_product.html",product=product)

@app.route('/delete_product',methods=['POST'])
def delete_product_post():
    id=request.args.get('id')
    pdao.delete(id)
    return redirect("/show_products")

@app.route('/product_delivery')
def product_delivery():
    id=request.args.get('id')
    product=pdao.get_one(id)
    return render_template("product_delivery.html",product=product)

@app.route('/product_delivery', methods=['POST'])
def product_delivery_post():
    id=request.args.get('id')
    count=request.form['x']
    pdao.delivery(id,count)
    return redirect("/show_products")

@app.route('/about')
def about():
    author=Author("Andrzej","Klusiewicz","klusiewicz@jsystems.pl")
    return render_template("about.html",author=author,products=pdao.get_all())


class Fruit(db.Model):
    __tablename__="fruits"
    fruit_id=db.Column(db.Integer,name="fruit_id",primary_key=True)
    fruit_name=db.Column(db.String,name="fruit_name",nullable=False)
    def __str__(self):
        return str(self.__dict__)

def get_fruits():
    return Fruit.query.all()
@app.route('/tests')
def tests():
    #db.create_all()
    # fruit1=Fruit()
    # fruit1.fruit_id=1
    # fruit1.fruit_name='banana'
    # db.session.add(fruit1)
    # fruit2 = Fruit()
    # fruit2.fruit_id = 2
    # fruit2.fruit_name = 'apple'
    # db.session.add(fruit2)
    # db.session.commit()
    for f in get_fruits():
        print(f)
    return "OK"



    # zwierze="toperz"
    # owoce=['banan','gruszka','melon','truskawka']
    # liczby=[random.randint(1,20) for e in range(10)]
    # f=Fruit("banana","yellow")
    # return render_template("tests.html", x=zwierze,fruits=owoce,numbers=liczby,fruit=f)
    # #return render_template("tests.html",x="nietoperz")

if __name__ == '__main__':
    app.run(debug=True,port=80)

#przerwa do 15:07

#51. Uruchom swoją aplikację na porcie 80 w trybie debug
#52. Dodaj do programu obsługe ekranów "/show_products", "/about", "/tests" i "/" (strona główna)
#53. Zadbaj o to by każdy ekran posiadał swój plik html i by był on pokazywany przy wejsciu na adres.
#    Każdy z tych plików html powinien mieć jakiś napis np. <h1>DUPA</h1>
#54. Zadbaj o to by na każdym ekranie było menu z linkami do wszystkich ekranów
#55. Przekaż do widoku /about swoje imię,nazwisko i email i wyświetl je na poziomie widoku
#56. W osobnym module "domain" stwórz klasę Author (pamiętaj o imporcie). Niech ta klasa posiada pola first_name,last_name, email.
#Dodaj do niej konstruktor sparametryzowany który będzie uzupełniał wszystkie pola obiektów tej klasy.
#Przerób kontroler ekranu about w taki sposob by nie przekazywac imienia, nazwiska, emaila osobno tylko
#poprzez obiekt który stworzysz (uzupełniajac przez konstruktor sparametryzowany) w kontrolerze.

#przerwa do 10:10

#57.W domenie stwórz klasę Product z polami product_id,name,price,opis,stock. Klasa Product powinna też posiadać
#konstruktor sparametryzowany oraz przesłoniętą metodę __str__.
# W kontrolerze ekranu show_products stwórz listę obiektów klasy Product i przeiteruj po niej wyświetlając
#na konsoli każdy z jej elementów

#58. Oddeleguj do metody get_all() w products_dao tworzenie (i zwracanie) listy obiektów klasy Product
# W kontrolerze ekranu show products wykorzystaj ta metodę do odebrania danych ktore wyswietlasz

#59. Wyświetl na ekranie show_products w tabelce nazwy, ceny i stany magazynowe wszystkich produktów

#60. Na liście produktów jeśli stan magazynowy jest zero to powininen się wyświetlać na czerwono pogrubiony,
#a jeśli nie jest równy zero to na ciemnozielono pogrubiony.


#przerwa do 11:34


#61. Dorób link prowadzący do ekranu szczegółów produktu - przekazując do niego id produktu przez pasek.
#W ekranie szczegółów produktu odbierz id i wyświetl je na konsoli.

#HTML + CSS

#62. Do product_dao dodaj funkcję get_one(id) która bedzie zwracała obiekt klasy Product. W kontrolerze widoku
# /product_details odbierz od funkcji z dao ten obiekt i przekaz do widoku. Na widoku wyswietl go w formie tabeli.

#63. Zadbaj o to by w ekranie listy produktów wyświetlić dane pochodzące z bazy

#PRZERWA OBIADOWA DO 13:22

#64. Zadbaj o to by wszystkie dane do łączenia się z bazą (host,hasło etc) pochodziły z jednego pliku konfiguracyjnego.

#65. Przerób funkcję get_one(id) w product_dao w taki sposób by pobierała dane z bazy.

#66. Na ekranie listy produktów dodaj link do dodawania produktu i stwórz do niego plik html i kontroler który wyswietli ten html

#67.Do formularza dodawania produktu dodaj pola do wprowadzania danych oraz guzik zatwierdzenia. Po
# naciśnięciu guzika zatwierdzenia chcemy odebrać dane z formularza i stworzyć obiekt klasy Product
# z tych danych. Następnie wyświetl obiekt na konsoli.

#Bootstrap

#PRZERWA DO 14:40

#68. Zadbaj o to żeby dane wprowadzane przez formularz dodawania produktu trafiały do bazy.

#69. Dodaj funkcjonalność kasowania produktów

#pandas, numpy, matplotlib


#70. Dodaj funkcjonalność dostawy. Z listy produktów ma być link do formularza dostawy i po
#wprowadzeniu ilości (której podanie jest wymagane a domyślna wartość wynosi zero) ekran powinien
#powrócić do listy produktów.
#1. Na liście produktów dodać link zawierający id produktu dla którego ma być dostawa
#2. Dodać kontroler obsługujący geta na /product_delivery z plikiem html który ma zostać wyświetlony
#3. Do pliku html dodaj formularz z wymaganym polem okreslajacym ilosc dostarczanych sztuk
#4. Dodaj kontroler obsługujący posta na /product_delivery.
#5. W obsłudze posta odczytaj id z paska i wartość która przyjdzie z formularza (wyprintuj sobie)
#6. Do product dao dodaj funkcję delivery przyjmującą przez argumenty id produktu i ilosc dostarczaną
#7. Przekaż z obsługi posta na /product_delivery dane o id i ilosci do stworzonej funkcji z dao
#8. Uruchom SQL który zmieni stan danego produktu:
#update produkty set stan=stan+x where id_produktu=y
#update produkty set stan=stan+10 where id_produktu=1


#przerwa do 10:34

