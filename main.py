from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', resultado="")

@app.route('/resultado', methods=['POST'])
def resultado():
    string = request.form['string']
    resultado = string[::-1]
    return render_template('index.html', resultado=f'{resultado}')

if __name__ == '__main__':
    app.run(debug=True)
