#!/usr/bin/env python

#-----------------------------------------------------------------------
# courses.py
# Author: Bob Dondero
#-----------------------------------------------------------------------
import flask
# import reg.sqlite
#-----------------------------------------------------------------------
# ask about the folder
app = flask.Flask(__name__, template_folder='.')

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    html_code = flask.render_template('searchpage.html')
    response = flask.make_response(html_code)
    #database handling here
    return response