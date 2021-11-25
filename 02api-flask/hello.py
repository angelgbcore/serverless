from flask import Flask
from flask import request
import usarMongoDB # aca importamos el archivo nuevo que interactua con la base
    print ('you are here')

app = Flask(__name__)


@app.route("/")
def hello():
        return "First Flask APP"

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():

    NBData = request.get_json()
    # Registro la fecha desde el lado del servidor
    NBData.update({"FECHA":datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
    # Inserto el valor en la base
    usarMongoDB.insertDatosNotebook(NBData)
    return 'JSON posted'