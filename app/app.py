import json
from os import path  # pip install notify-py
from typing import Dict, List

import mysql.connector
from flask import (Flask, redirect, render_template,  # pip install Flask
                   request, session, url_for, make_response,jsonify)

EJER = {
    "ejercicio1":"sentadilla",
    "ejercicio2":"lagartija",
    "ejercicio3":"abdomilas",
    "ejercicio4":"levantamiento"
}

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
def test_table() -> List[Dict]:
    config = {
        'user': 'uynv2tnynvplpgon',
        'password': '8rzJP0pyuiq1VkMLELfx',
        'host': 'b0manp20m3mu8n6jdwgo-mysql.services.clever-cloud.com',
        'port': '3306',
        'database': 'b0manp20m3mu8n6jdwgo'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM test_table')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
        #return json.dumps({'test_table': test_table()})
        #return render_template("contenido.html")
        return render_template("contenido.html", res = EJER)
@app.route('/layout', methods = ["GET", "POST"])
def layout():
    session.clear()
    return render_template("contenido.html")

@app.route('/login', methods= ["GET", "POST"])
def login():
    #notificacion = Notify()

    if request.method == 'POST':
        config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'devopsroles'
             }
        connection = mysql.connector.connect(**config)

        ejercicio = request.form['ejercicio']
        nombreEjer = request.form['nombreEjer']

        cur = connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s",(email,))
        user = cur.fetchone()
        cur.close()
        
        if len(user)>0:
            if password == user[3]:
                session['name'] = user[1]
                session['email'] = user[2]
                session['tipo'] = user[4]

                if session['tipo'] == 1:
                    return render_template("premium/home.html")
                elif session['tipo'] == 2:
                    return render_template("estandar/homeTwo.html")


            else:
                #notificacion.title = "Error de Acceso"
                #notificacion.message="Correo o contraseña no valida"
                #notificacion.send()
                return render_template("login.html")
        else:
            #notificacion.title = "Error de Acceso"
            #notificacion.message="No existe el usuario"
            #notificacion.send()
            return render_template("login.html")
    else:        
        return render_template("login.html")


@app.route('/registro', methods = ["GET", "POST"])
def registro():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'devopsroles'
             }
    connection = mysql.connector.connect(**config)
    cur = connection.cursor()
    cur.execute("SELECT * FROM tip_usu")
    tipo =[{'id_tip_usu':id_tip_usu,'nom_tip_usu': nom_tip_usu} for (id_tip_usu, nom_tip_usu) in cur] 

    cur = connection.cursor()
    cur.execute("SELECT * FROM sexo_interes")
    interes = [{'id_sex':id_sex,'nom_sex': nom_sex} for (id_sex, nom_sex) in cur]
    cur.close()

    #notificacion = Notify()
    
    

    if request.method == 'GET':
        return render_template("registro.html", tipo = tipo, interes = interes )
    
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        tip = request.form['tipo']
        interes = request.form['interes']  
        config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'devopsroles'
             }
        connection = mysql.connector.connect(**config)
        cur = connection.cursor()
        cur.execute("INSERT INTO users (name, email, password, id_tip_usu, interes) VALUES (%s,%s,%s,%s,%s)", (name, email, password,tip,interes,))
        connection.commit()
        #notificacion.title = "Registro Exitoso"
        #notificacion.message="ya te encuentras registrado en 🤵 MORE LOVE 👰, por favor inicia sesión y empieza a descubrir este nuevo mundo."
        #notificacion.send()
        return redirect(url_for('login'))

@app.route("/ObtenerEjercicios")
def get_ejercicios():
    res = make_response(jsonify(EJER),200)
    return res

@app.route("/ObtenerEjercicio/<ejercicio>")
def get_ejercicio(ejercicio):
    if ejercicio in EJER:
        res = EJER.get(ejercicio)
        return make_response(jsonify({"res":res}),200)

    res = make_response(jsonify({"error":"not found"}),400)
    return res

@app.route("/AgregarEjer/<ejercicio>",methods=["POST"])
def post_ejercicio(ejercicio):
    req = request.get_json()

    if ejercicio in EJER:
        res = make_response(jsonify({"error": "El ejercicio ya existe"}))
        return res

    EJER.update(req)

    res = make_response(jsonify({"message" : "ejercicio creato"}),201)
    return res

@app.route("/ModificarEjer/<ejercicio>",methods=["PUT"])
def update_ejercicio(ejercicio):
    req = request.get_json()

    if ejercicio in EJER:
        EJER[ejercicio] = req["new"]
        res = make_response(jsonify({"res": EJER[ejercicio]}),200)
        return res

    res = make_response(jsonify({"error" : "no se pudo modificar"}),400)
    return res

@app.route("/eliminarEjercicio/<ejercicio>", methods=["DELETE"])
def Delete_ejercicio(ejercicio):

    if ejercicio in EJER:
        del EJER[ejercicio]
        res = make_response(jsonify(EJER),200)
        return res



#if __name__ == '__main__':
#    app.run(host='0.0.0.0')