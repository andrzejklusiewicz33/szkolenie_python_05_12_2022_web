from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")#'<h1>Strona główna</h1>'

@app.route('/show_employees')
def show_employees():
    return '<h1>Lista pracowników</h1>'

@app.route('/show_products')
def show_products():
    return "<h1>Lista produktów</h1>"

@app.route('/about')
def about():
    return "<h1>Strona o programie</h1>"

@app.route('/tests')
def tests():
    return "<h1>Strona do testów</h1>"

if __name__ == '__main__':
    app.run(debug=True,port=80)

#przerwa do 15:07

#51. Uruchom swoją aplikację na porcie 80 w trybie debug
#52. Dodaj do programu obsługe ekranów "/show_products", "/about", "/tests" i "/" (strona główna)
#53. Zadbaj o to by każdy ekran posiadał swój plik html i by był on pokazywany przy wejsciu na adres.
#    Każdy z tych plików html powinien mieć jakiś napis np. <h1>DUPA</h1>