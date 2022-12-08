from flask import Flask,render_template
import random
from domain import *
import employees_dao as edao

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")#'<h1>Strona główna</h1>'

@app.route('/show_employees')
def show_employees():
    employees=edao.get_all()
    for e in employees:
        print(e)
    return render_template("show_employees.html")

@app.route('/show_products')
def show_products():
    products=[]
    p1=Product(1,"Bulbulator",1000,"robi bul bul",10)
    products.append(p1)
    p2=Product(2,"Przyczłap do bulbulatora",200,"Taki wihajster co ten no wiadomo",2)
    products.append(p2)
    p3=Product(3,"Dzyndzel do przyczłapa",50,"Taki teges z tym że ten",0)
    products.append(p3)
    for p in products:
        print(p)
    return render_template("show_products.html")

@app.route('/about')
def about():
    author=Author("Andrzej","Klusiewicz","klusiewicz@jsystems.pl")
    return render_template("about.html",author=author,products=pdao.get_all())


@app.route('/tests')
def tests():
    zwierze="toperz"
    owoce=['banan','gruszka','melon','truskawka']
    liczby=[random.randint(1,20) for e in range(10)]
    f=Fruit("banana","yellow")
    return render_template("tests.html", x=zwierze,fruits=owoce,numbers=liczby,fruit=f)
    #return render_template("tests.html",x="nietoperz")

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