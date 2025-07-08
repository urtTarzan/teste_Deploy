from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/destino')
def destino():
    return render_template('destino.html')


app.run(host='0.0.0.0')