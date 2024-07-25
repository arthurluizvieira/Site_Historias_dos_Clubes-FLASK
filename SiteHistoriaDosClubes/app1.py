from flask import Flask, render_template

app1 = Flask(__name__)

@app1.route('/')
def home():
    return render_template('home.html')


@app1.route('/santos')
def santos():
    return render_template('santos.html')

@app1.route('/saopaulo')
def saopaulo():
    return render_template('saopaulo.html')

@app1.route('/palmeiras')
def palmeiras():
    return render_template('palmeiras.html')

if __name__ == '__main__':
    app1.run(debug=True, port=5001)

