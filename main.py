from flask import Flask, redirect, request, make_response, redirect, render_template

app = Flask(__name__, template_folder="./src")

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response 

@app.route('/hello')
def hello():
    #return "Hello world Flask hoy mas"
    user_ip = request.cookies.get('user_ip')
    return 'Esta es tu dirección IP desde donde nos visitas: {}'.format(user_ip)
    #Otra manera de dar formato es:
        #return f'Hello World Gente, tu IP es{user_ip}'

@app.route('/docente')
def docente():
    return render_template("docente/views/menu.html")

@app.route('/docente/asignaturas-propias')
def asignaturas_propias():
    return render_template("docente/views/asignaturas.html")

@app.route('/docente/datos-personales', methods=["GET","POST"])
def datos_personales():
    return render_template("docente/views/datos-personales.html")

@app.route('/docente/estudiantes')
def estudiantes():
    return render_template("docente/views/estudiantes.html")

#las siguientes dos lineas sirven para debuggear el servidor y acepte cambios al instante sin parar el server
if __name__ == '__main__':
    app.run(debug=True)
app.run()