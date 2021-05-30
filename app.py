#Importaciones
from flask import Flask, request

app = Flask(__name__)

app.secret_key = '54SF4GHAFHGAS4'

app.run(debug=True, port=5000)