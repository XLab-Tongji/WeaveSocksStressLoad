#! /usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
import sh


scenario_comment = {
    "scenario1": "登陆-浏览-创建订单-查看订单-支付",
    "scenario2": "浏览",
    "scenario3": "注册-登陆",
}


app = Flask(__name__)


@app.route('/scenario1/<current_num>/<total_num>')
def scenario1(current_num, total_num):
    print scenario_comment['scenario1']
    sh.Command("locust -f scenario1.py -c %s -r %s -n %s --no-web --only-summary > scenario1.log" %
                (current_num, current_num, total_num))


@app.route('/scenario2/<current_num>/<total_num>')
def scenario2(current_num, total_num):
    print scenario_comment['scenario2']
    sh.Command("locust -f scenario2.py -c %s -r %s -n %s --no-web --only-summary > scenario2.log" %
               (current_num, current_num, total_num))


@app.route('/scenario2/<current_num>/<total_num>')
def scenario3(current_num, total_num):
    print scenario_comment['scenario3']
    sh.Command("locust -f scenario3.py -c %s -r %s -n %s --no-web --only-summary > scenario3.log" %
               (current_num, current_num, total_num))

if __name__ == '__main__':
    app.run()
