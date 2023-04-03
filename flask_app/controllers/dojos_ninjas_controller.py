from flask import Flask, render_template, redirect, request
from flask_app import app

#importamos modelos
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all_dojos()
    return render_template('index.html', dojos=dojos)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    #request.form = {name: "Colombia"}
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_all_dojos()
    return render_template('ninjas.html', dojos=dojos)

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {'id': id}
    dojo = Dojo.get_dojo_with_ninja(data)
    return render_template('dojo.html', dojo=dojo)