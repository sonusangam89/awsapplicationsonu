# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 09:44:18 2023

@author: aspdi
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')

def myapp():
    return "AWS CI/CD pipeline"

if __name__ == '__main__':
    app.run(host='0.0.0.0')