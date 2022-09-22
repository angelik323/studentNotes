from flask import Flask, redirect, request, make_response, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/login'))
    response.set_cookie('user_ip', user_ip)

    return response 

@app.route('/login')
def login():
    #return "Hello world Flask hoy mas"
    #user_ip = request.cookies.get('user_ip')
    return render_template('login.html')
    #Otra manera de dar formato es:
        #return f'Hello World Gente, tu IP es{user_ip}'

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/teachers')
def teachers():
    return render_template('teachers.html')

@app.route('/admon')
def admon():
    return render_template('admon.html')

#las siguientes dos lineas sirven para debuggear el servidor y acepte cambios al instante sin parar el server
if __name__ == '__main__':
    app.run(debug=True)
app.run()