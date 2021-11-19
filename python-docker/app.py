import requests
import json
from flask import Flask
app = Flask(__name__)


metaurl='http://169.254.169.254/latest/meta-data'



@app.route('/')
def hello_world():
    node=requests.get(f'{metaurl}/local-hostname').text
    localip=requests.get(f'{metaurl}/local-ipv4').text
    return f'''
Node: {node}
<br>IP: {localip}
    '''


app.run(host='0.0.0.0', port=8080, debug=True, ssl_context=None)
