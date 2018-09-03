#! /usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
import os


app = Flask(__name__)

@app.route('/all/<host>/<current_num>/<total_num>')
def scenario_all(host, current_num, total_num):
    re = os.system("locust -f ./scenario/scenario_all.py --host=%s -c %s -r %s -n %s --no-web --only-summary > scenario2.log" %
        (host, current_num, current_num, total_num))
    return  'success'


@app.route('/login/<host>/<current_num>/<total_num>')
def scenario_login(host, current_num, total_num):
    re = os.system("locust -f ./scenario/scenario_login.py --host=%s -c %s -r %s -n %s --no-web --only-summary > scenario2.log" %
        (host, current_num, current_num, total_num))
    return 'success'


@app.route('/browse/<host>/<current_num>/<total_num>')
def scenario_browse(host, current_num, total_num):
    re = os.system("locust -f ./scenario/scenario_browse.py --host=%s -c %s -r %s -n %s --no-web --only-summary > scenario2.log" %
        (host, current_num, current_num, total_num))
    return 'success'


@app.route('/test')
def test():
    os.system("pwd")
    os.system("ls -l")
    return "Success: System is running..."


if __name__ == '__main__':
    app.run()
