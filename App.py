#appy.py 
from flask import Flask, render_template
import os

app= Flask(__name__)
@app.route('/')
def hello():
    return 'Hola desde Raylway en Python'

@app.route('/index')
def home():
    dato = "Mi dato"
    return render_template('index.html' , dato = dato)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))