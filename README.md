## 参考命令
```
locust --host=http://10.60.38.181:30001 -f ./locustfile.py --clients=1000 --hatch-rate=5 --num-request=1000 --no-web --only-summary

locust -f ./locustfile.py --clients=1000 --hatch-rate=5 --num-request=1000 --no-web --only-summary

locust -f ./locustfile.py -c 1 -r 1 -n 3 --no-web --only-summary
```

## LOCUST 方案设计

无界面方案

### 场景
1. scenario1: 登陆-浏览-创建订单-查看订单-支付
2. scenario2: 注册-登陆
3. scenario3: 浏览

### 参数
1. 服务器地址
1. 并发用户数
2. 总的请求数

### API
1. `/all/<host>/<current_num>/<total_num>`
2. `/login/<host>/<current_num>/<total_num>`
3. `/browse/<host>/<current_num>/<total_num>`
4. `/test`