from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/healthcheck')
def healthcheck():
    return "OK", 200
