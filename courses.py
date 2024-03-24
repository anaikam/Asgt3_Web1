#!/usr/bin/env python

#-----------------------------------------------------------------------
# courses.py
# Author: Bob Dondero
#-----------------------------------------------------------------------
import flask
import database
from regdetails import class_details 
import sys
#-----------------------------------------------------------------------
# ask about the folder
# https://www.w3schools.com/html/html_tables.asp - put this in readme
app = flask.Flask(__name__, template_folder='.')

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    dept = flask.request.args.get('dept')
    num = flask.request.args.get('coursenum')
    area = flask.request.args.get('area')
    title = flask.request.args.get('title')
    try:
        if dept == None:
            dept = ""
        if num == None:
            num = ""
        if area == None:
            area = ""
        if title == None:
            title = ""
        table = database.course_overviews(dept, num, area, title)
    #handle error cases
        html_code = flask.render_template('searchpage.html', table=table,
        dept=dept, coursenum=num, area=area, title=title)
        response = flask.make_response(html_code)
        response.set_cookie('prev_dept', dept)
        response.set_cookie('prev_num', num)
        response.set_cookie('prev_area', area)
        response.set_cookie('prev_title', title)
    #database handling here
        return response
    except Exception as ex:
        html_code = flask.render_template('error.html', ex = ex, message = "A server error occurred. Please contact the system administrator.")
        print(str(ex), file=sys.stderr)
        response = flask.make_response(html_code)
        return response

@app.route('/regdetails', methods=['GET'])
def regdetails():
    # do a if classid is None check
    # dont convert to int
    classid = flask.request.args.get('classid')
    dept = flask.request.cookies.get('prev_dept')
    num = flask.request.cookies.get('prev_num')
    area = flask.request.cookies.get('prev_area')
    title = flask.request.cookies.get('prev_title')
    print(type(classid))
    if classid == '' or classid == None:
        html_code = flask.render_template('error.html', message = "missing classid")
        response = flask.make_response(html_code)
        return response
    
    elif classid.isdigit()== False:
        html_code = flask.render_template('error.html', message = "non-integer classid")
        response = flask.make_response(html_code)
        return response
    else:
        try: 
            general_table, prof_table, dept_table = class_details(classid)
            department_table = []
            for row3 in dept_table:
                        if general_table[0][0] == row3[0]:
                            department_table.append([row3[1], row3[2]])
            professors_table = []
            for row2 in prof_table:
                        if general_table[0][0] == row2[0]:
                            professors_table.append(row2[1])
            html_code = flask.render_template('regdetails.html', classid=classid, general_table=general_table[0], prof_table=professors_table,dept_table=department_table, dept=dept, area=area, coursenum=num, title=title)
            response = flask.make_response(html_code)
            return response
        except Exception as ex:
            html_code = flask.render_template('error.html', ex = ex, message = "no class with classid "+classid+" exists")
            print(str(ex), file=sys.stderr)
            response = flask.make_response(html_code)
            return response

# @app.route('/errors', methods=['GET'])
# def errors():

    