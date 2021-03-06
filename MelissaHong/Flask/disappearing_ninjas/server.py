from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
url_for = 'static'

ninjaturtles = {'blue':'/static/leonardo.jpg', 'orange':'michelangelo.jpg', 'red':'raphael.jpg', 'purple':'donatello.jpg', 'april':'notapril.jpg'}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    data = ninjaturtles
    show = ninjaturtles
    data.pop('april')
    return render_template('ninja.html', show = data)

@app.route('/ninja/<ninjaturtle>', methods = ['GET'])
def show(ninjaturtle):
    data = {}
    if ninjaturtle == 'blue' or ninjaturtle == 'orange' or ninjaturtle == 'red' or ninjaturtle =='purple':
        data[ninjaturtle] = ninjaturtles[ninjaturtle]
    else:
        data['april'] = ninjaturtles['april']

    return render_template("ninja.html", show = data)

if __name__ == '__main__':
    app.run(debug=True)
