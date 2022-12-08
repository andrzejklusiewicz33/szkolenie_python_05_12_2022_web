from flask import Flask,render_template
import random
from domain import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")#'<h1>Strona główna</h1>'

@app.route('/show_employees')
def show_employees():
    employees=[]
    e1=Employee(1,"Ferdynand","Kiepski",6000,"jakiś długi komentarz do pracownika. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. ")
    employees.append(e1)
    e2 = Employee(2, "Młody", "Kiepski", 3000,"jakiś długi komentarz do pracownika. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. ")
    employees.append(e2)
    e3 = Employee(3, "Babka", "Kiepska", 8000,"jakiś długi komentarz do pracownika. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. Srutututu pęczek drutu. ")
    employees.append(e3)
    for e in employees:
        print(e)
    return render_template("show_employees.html")

@app.route('/show_products')
def show_products():
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