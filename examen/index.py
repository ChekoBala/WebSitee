from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def index_():
    return render_template('login.html')

@app.route('/login.html')
def pagina():
    return render_template('login.html')  


if __name__ == '__main__':
    app.run(port=4000, host ='0.0.0.0')