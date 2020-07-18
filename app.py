from __future__ import unicode_literals, print_function
from flask import Flask, render_template,request
import plac
import random
from pathlib import Path
import spacy
from tqdm import tqdm 
import spacy
from spellchecker import SpellChecker
import re

konjac_dir='Konjac NER'
bb_cream_dir='BB Cream NER'
nlp1=spacy.load(konjac_dir)
nlp2=spacy.load(bb_cream_dir)
app = Flask(__name__)
#app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')

#app.logger.addHandler(logging.StreamHandler(sys.stdout))
#app.logger.setLevel(logging.ERROR)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/konjac')
def konjac():
    return render_template('konjac.html')

@app.route('/bb_cream')
def bb_cream():
    return render_template('bb_cream.html')

@app.route('/answer_konjac',methods=['POST'])
def konjac_ans():
    rev=request.form['konjactext']

    r=nlp1(rev.lower())

    
    l=[ent.label_  for ent in r.ents]

    if len(l)>0:
        return render_template('konjac_answer.html',answer="This product is a "+str(l[0]))
    else:
        return render_template('konjac_answer.html',answer="Could not find product")

@app.route('/bb_cream_ans',methods=['POST'])
def bb_cream_ans():
    rev=request.form['bbtext']

    r=nlp2(rev.lower())

    l=[ent.label_  for ent in r.ents]

    if len(l)>0:
        return render_template('bb_ans.html',answer="This product is a "+str(l[0]))
    else:
        return render_template('bb_ans.html',answer="Could not find product")