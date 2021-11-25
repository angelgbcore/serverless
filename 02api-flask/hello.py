from flask import Flask
from flask import request
    print ('you are here')
app = Flask(__name__)

@app.route("/")
def hello():
        return "First Flask APP"

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    print ('Getting RAW Data')
    print request.get_data()
    print ('Validate JSON Format')
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'