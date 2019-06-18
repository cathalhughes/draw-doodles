from flask import Flask, request, Response, render_template, flash, redirect, url_for, jsonify
import ssl
from flask_cors import CORS
import requests
import json



ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ctx.load_cert_chain('ssl.crt', 'ssl.key')

app = Flask(__name__)
app.secret_key = "MY_SECRET_KEY"
CORS(app, resources={r"/*": {"origins": "*"}}, send_wildcard=True)

@app.route('/')
def index():
    return render_template("index.html")

app.run(host='localhost', port=5000) #ssl_context=ctx ,threaded=True, debug=True)