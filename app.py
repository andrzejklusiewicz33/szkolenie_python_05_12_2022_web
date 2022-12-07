from flask import Flask

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():  # put application's code here
    return 'Hello Mapet! Cośtam'


if __name__ == '__main__':
    app.run(debug=True,port=80)

#przerwa do 15:07

#51. Uruchom swoją aplikację na porcie 80 w trybie debug