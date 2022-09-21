from flask import Flask, redirect, request, make_response, redirect

app = Flask(__name__)

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

#las siguientes dos lineas sirven para debuggear el servidor y acepte cambios al instante sin parar el server
if __name__ == '__main__':
    app.run(debug=True)
app.run()