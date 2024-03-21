#!/usr/bin/env python

#-----------------------------------------------------------------------
# courses.py
# Author: Bob Dondero
#-----------------------------------------------------------------------
import flask
import database
import regdetails
#-----------------------------------------------------------------------
# ask about the folder
# https://www.w3schools.com/html/html_tables.asp - put this in readme
app = flask.Flask(__name__, template_folder='.')

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    dept = flask.request.args.get('dept')
    number = flask.request.args.get('num')
    area = flask.request.args.get('area')
    title = flask.request.args.get('title')
    table = database.course_overviews(dept, number, area, title)
    #handle error cases
    html_code = flask.render_template('searchpage.html', table=table)
    response = flask.make_response(html_code)
    #database handling here
    return response

@app.route('/coursedetails', methods=['GET'])
def coursedetails():
    classid = flask.request.args.get('classid')
    general_table, prof_table, dept_table = regdetails.class_details(int(classid))
    html_code = flask.render_template('coursedetails.html', general_table=general_table, prof_table=prof_table, dept_table=dept_table)
    response = flask.make_response(html_code)

    return response

# @app.route('/errors', methods=['GET'])
# def errors():

    