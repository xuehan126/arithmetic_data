#! /usr/bin/python3
def decorator(func):
    def wrapper(*args,**kwargs):
        arg = func(*args, **kwargs)
        username = input("please input username: ")
        passwd = input("please input passwd: ")
        flags = 0
        if username == arg["username"] and passwd == arg["passwd"]:
            print("login success! ")
            flags = 1
            return True
            
        print("login failed!")
        flags = 2
        return False
    return wrapper

@decorator
def login(kwargs):
    return kwargs
# login({"username": "xuehan", "passwd": "123456"})

@decorator
def shoppingCar():
    unit_price_every_projuct = {
        "skiping-car": 1388,
        "macbookpro": 7188,
        "applewatch": 3888,
        "jecket": 288
    }
    if flags == 1:
        print("进入个人中心！")
    if flags == 2:
        print("输入账号或密码错误")
shoppingCar()
    
