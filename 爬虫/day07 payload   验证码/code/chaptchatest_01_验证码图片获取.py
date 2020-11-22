"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/29'
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
from selenium import webdriver
from PIL import Image

def get_captchar():
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com')
    browser.save_screenshot('./images/baidu.png')
    element=browser.find_element_by_xpath('//div[@id="lg"]/img[1]')
    #location办法可能会有偏移，但是每次都会锁定了了验证码的位置，所以稍微修正一下location的定位，后面都管用
    left = element.location['x']#验证码图片左上角横坐标
    top = element.location['y']#验证码图片左上角纵坐标
    right = left + element.size['width']#验证码图片右下角横坐标
    bottom = top + element.size['height']#验证码图片右下角纵坐标

    #rangle=(806,382,913,415)#手工方法有时候可以，但是有时候也会出现第一次可以，但是后面各种偏移定位不准的奇葩现象
    im=Image.open('./images/baidu.png')
    im_crop=im.crop((left,top,right,bottom))#这个im_crop就是从整个页面截图中再截出来的验证码的图片
    im_crop.save('./images/logo.png')
    browser.quit()

get_captchar()