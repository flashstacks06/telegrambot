from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('nueva_variable')
def handle_nueva_variable(data):
    # Obtener la nueva variable desde los datos recibidos
    nueva_variable = data['nueva_variable']

    # Lógica adicional con la nueva variable si es necesario

    # Enviar la nueva variable al cliente para activar la función
    socketio.emit('activar_funcion', {'valor': nueva_variable})

if __name__ == '__main__':
    socketio.run(app)
