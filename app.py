import pandas as pd
import nltk
from flask import request
from flask import jsonify
from flask import Flask, render_template
import re


app = Flask(__name__,template_folder='templates')

@app.route('/')
def my_form():
    return render_template('index.html')


# @app.route('/', methods=['GET','POST'])
# def my_form_post():
#     file = open('svenska-ord.txt', encoding='utf-8')
#     text = request.form['text']
#     pattern = f'^{text}'
#     words = []
#     for line in file.readlines():
#         if re.findall(pattern, line.rstrip('\n')):
#            line = words.append(line.rstrip('\n'))
#     return(render_template('index.html', variable=words))

@app.route('/', methods=['GET','POST'])
def my_form_post():
    file = open('svenska-ord.txt', encoding='utf-8')
    text = request.form['text']
    pos = list(text)
    words = []
    if len(pos) <= 3:
        pat1 = f'^{pos[0]}{pos[1]}{pos[2]}$'
        for line in file.readlines():
            if re.findall(pat1, line.rstrip('\n')):
                line = words.append(line.rstrip('\n'))
    elif len(pos) <= 4:
        pat2 = f'^{pos[0]}{pos[1]}{pos[2]}{pos[3]}$'
        for line in file.readlines():
            if re.findall(pat2, line.rstrip('\n')):
                line = words.append(line.rstrip('\n'))
    elif len(pos) <= 5:
        pat3 = f'^{pos[0]}{pos[1]}{pos[2]}{pos[3]}{pos[4]}$'
        for line in file.readlines():
            if re.findall(pat3, line.rstrip('\n')):
                line = words.append(line.rstrip('\n'))
    elif len(pos) <= 6:
        pat4 = f'^{pos[0]}{pos[1]}{pos[2]}{pos[3]}{pos[4]}{pos[5]}$'
        for line in file.readlines():
            if re.findall(pat4, line.rstrip('\n')):
                line = words.append(line.rstrip('\n'))
    return(render_template('index.html', complete_words=words))

if __name__ == "__main__":
    app.run(port='8088',threaded=False)
