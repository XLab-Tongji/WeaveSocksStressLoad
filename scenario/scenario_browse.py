# -*- coding:utf-8 -*-
import base64

from locust import HttpLocust, TaskSet, task
from random import randint, choice

# 定义用户行为，继承TaskSet类，用于描述用户行为
# (这个类下面放各种请求，请求是基于requests的，每个方法请求和requests差不多，请求参数、方法、响应对象和requests一样的使用，url这里写的是路径)
# client.get===>requests.get
# client.post===>requests.post

class wsTest(TaskSet):
    # task装饰该方法为一个事务方法的参数用于指定该行为的执行权重。参数越大，每次被虚拟用户执行概率越高，不设置默认是1，
    @task
    def test_1(self):
        catalogue = self.client.get("/catalogue").json()
        category_item = choice(catalogue)
        item_id = category_item["id"]

        self.client.get("/")
        self.client.get("/category.html")
        self.client.get("/detail.html?id={}".format(item_id))
        self.client.delete("/cart")
        self.client.post("/cart", json={"id": item_id, "quantity": 1})
        self.client.get("/basket.html")

# 这个类类似设置性能测试，继承HttpLocust
class websitUser(HttpLocust):
    # 指向一个上面定义的用户行为类
    task_set = wsTest
    #执行事物之间用户等待时间的下界，单位毫秒，相当于lr中的think time
    min_wait = 3000
    max_wait = 6000
    host = 'http://10.60.38.181:30001'
