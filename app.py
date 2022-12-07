from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return '<h1>Strona główna</h1>'

@app.route('/show_employees')
def show_employees():
    return '<h1>Lista pracowników</h1>'

if __name__ == '__main__':
    app.run(debug=True,port=80)

#przerwa do 15:07

#51. Uruchom swoją aplikację na porcie 80 w trybie debug
#52. Dodaj do programu obsługe ekranów "/show_products", "/about", "/tests" i "/" (strona główna)