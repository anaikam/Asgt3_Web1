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
    try:
        table = database.course_overviews(dept, number, area, title)
    #handle error cases
        html_code = flask.render_template('searchpage.html', table=table)
        response = flask.make_response(html_code)
    #database handling here
        return response
    except Exception as ex:
        html_code = flask.render_template('error.html', ex = ex)
        print(str(ex), file=sys.stderr)
        response = flask.make_response(html_code)
        return response

@app.route('/coursedetails?classid=', methods=['GET'])
def coursedetails():
    # How do we collect classid and how do we collect errors
    
    print(type(classid))
    # do a if classid is None check
    # dont convert to int
    general_table, prof_table, dept_table = regdetails.class_details(classid)
    html_code = flask.render_template('coursedetails.html', classid=classid)
    # html_code = flask.render_template('coursedetails.html', general_table=general_table, prof_table=prof_table, dept_table=dept_table)
    response = flask.make_response(html_code)

    return response

# @app.route('/errors', methods=['GET'])
# def errors():

    