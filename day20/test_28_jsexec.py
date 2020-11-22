"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/13'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import execjs
import os

if __name__ == '__main__':
    print(execjs.eval("new Date"))

    #获取 当前 执行JS的环境的名字
    print(execjs.get().name)
    #  设置js 执行的环境
    os.environ["EXECJS_RUNTIME"] = "PhantomJS"
    print(execjs.get().name)
    print(execjs.eval("Date.now()"))

    #  compile里为 js 语句
    ctx = execjs.compile("""            
            function add(x, y) {
                    return x + y;
               }
    """)
    #  compile 会返回一个上下文执行的环境  通过 call 方法执行 指定的函数

    result = ctx.call("add", 1, 2)
    print(result)
    # 通过execjs  执行多个 js  语句   
    print(execjs.exec_("var a=100;var b=201;return a+b;"))

