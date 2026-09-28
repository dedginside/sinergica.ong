from flask import Flask, render_template
#importar la librería flask y elementos del paquete
#flask: es el general. render_template: para renderizar archivos HTML y enviarlos al usuario

app = Flask(__name__)
#instancia clase flask. objeto clase principal. (__name__): es un valor de python para determinar el estado del archivo
#las instancias son POO. así que app ahora tiene atributos de flask
@app.route("/")
#decorador de Flask para relacionar una URL con la raíz de la página web
#las funciones se ejecutan de forma líneal después del @app.route("/")
def index():
    return render_template("index.html")
#define la función a ejecutar con el @app.route, inicializa la web
if __name__ == "__main__":
    app.run(debug=True)
#ejecuta un condicional para asegurarse de que el archivo no es importado de otro módulo