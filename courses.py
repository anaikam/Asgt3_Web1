#!/usr/bin/env python

#-----------------------------------------------------------------------
# courses.py
# Author: Bob Dondero
#-----------------------------------------------------------------------
import flask
# import reg.sqlite
#-----------------------------------------------------------------------
# ask about the folder
app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/searchpage', methods=['GET'])
def searchpage():
    html_code = flask.render_template('searchpage.html')
    response = flask.make_response(html_code)
    return response