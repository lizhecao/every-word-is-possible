#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, request, make_response  
from hashlib import sha1
app = Flask(__name__)

def check_signature(signature, timestamp, nonce):
    L = [timestamp, nonce, token]
    L.sort()
    s = L[0] + L[1] + L[2]
    return hashlib.sha1(s).hexdigest() == signature
 

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/check',  methods=['GET', 'POST'])  
def check():  
    if request.method == 'GET':  
        token = r'test' # 这个根据自己的设置自行修改  
        signature = request.args.get('signature', '')  
        echostr = request.args.get('echostr', '')  
        timestamp = request.args.get('timestamp', '')  
        nonce = request.args.get('nonce', '')  
        tmp = [timestamp, nonce, token]  
        tmp.sort()  
        tmp = ''.join(tmp)  
        if signature == sha1(tmp).hexdigest():  
            return  make_response(echostr)  
        else:  
            return "Access denied."  
 
if __name__ == "__main__":
    app.run()