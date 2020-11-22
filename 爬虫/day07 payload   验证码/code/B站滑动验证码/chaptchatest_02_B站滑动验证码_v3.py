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

import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from io import BytesIO
from PIL import Image
from chaojiying import Chaojiying


CHAOJIYING_USERNAME = 'Thompson'
CHAOJIYING_PASSWORD = 'Thompson'
CHAOJIYING_SOFT_ID = '1bce712d583f72be3a40d5960a86c94f'
CHAOJIYING_KIND = 9101

class Crack():
    def __init__(self, username, passwd):
        self.url = 'https://passport.bilibili.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 100)
        self.BORDER = 31
        self.passwd = passwd
        self.username = username
        self.chaojiying = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID)

    def open(self):
        """
        打开浏览器,并输入查询内容
        """
        self.browser.get(self.url)
        keyword = self.wait.until(EC.presence_of_element_located((By.ID, 'login-username')))
        keyword.send_keys(self.username)
        keyword = self.wait.until(EC.presence_of_element_located((By.ID, 'login-passwd')))
        keyword.send_keys(self.passwd)
        btn = self.browser.find_element_by_xpath('//a[@class="btn btn-login"]')
        btn.click()

    def get_images(self, bg_filename='bg.png'):
        """
        获取验证码图片
        :return: 图片的location信息
        """
        time.sleep(2)
        self.browser.save_screenshot(bg_filename)
        element = self.browser.find_element_by_xpath('//canvas[@class="geetest_canvas_bg geetest_absolute"]')
        location = element.location
        size = element.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
        print('验证码位置', top, bottom, left, right)
        screenshot = Image.open(bg_filename)
        # 截取验证码图片
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save("./images/bzyzm.png")


    def get_gap(self):
        """
        获取缺口偏移量
        :param img1: 不带缺口图片
        :param img2: 带缺口图片
        :return:
        """
        # 识别验证码
        im = open('./images/bzyzm.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        result = self.chaojiying.post_pic(im, CHAOJIYING_KIND)
        print(result)
        result = result.get('pic_str').split(',')
        result = int(result[0])
        return int(result)


    def get_track(self, distance):
        """
        根据偏移量获取移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 0.7
        # 计算间隔
        t = 0.05
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 18
            else:
                # 加速度为负3
                a = -6
            # 初速度v0
            v0 = v
            # 当前速度v = v0 + at
            v = v0 + a * t
            # 移动距离x = v0t + 1/2 * a * t^2
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
            print('forword', current, distance)

        v = 0

        move = current - distance
        # 加入轨迹
        track.append(round(move))


        return track

    def get_slider(self):
        """
        获取滑块
        :return: 滑块对象
        """
        while True:
            try:
                slider = self.browser.find_element_by_xpath('//div[@class="geetest_slider_button"]')
                break
            except:
                time.sleep(0.5)
        return slider

    def move_to_gap(self, slider, track):
        """
        拖动滑块到缺口处
        :param slider: 滑块
        :param track: 轨迹
        :return:
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        while track:
            x = random.choice(track)
            #x=track.pop(0)
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
            track.remove(x)
            time.sleep(0.005)
        time.sleep(2)
        print('release')
        ActionChains(self.browser).release(slider).perform()
        time.sleep(2)
        #self.browser.quit()

    def crack(self):
        # 打开浏览器
        self.open()

        # 保存的图片名字
        bg_filename = './images/bg.png'
        fullbg_filename = './images/fullbg.png'

        # 获取图片
        self.get_images(bg_filename)
        # 获取缺口位置
        gap = self.get_gap()
        print('缺口位置', gap)

        track = self.get_track(gap - self.BORDER)
        print('滑动滑块')
        #print(track)

        # 点按呼出缺口
        slider = self.get_slider()
        # 拖动滑块到缺口处
        self.move_to_gap(slider, track)
        #
        time.sleep(1)
        try:
            mspan = self.browser.find_elements_by_class_name('gt_info_content')
            if len(mspan) > 0:
                info = mspan.text
                print('info:',info)
                if '怪物吃了拼图' in info:
                    print(mspan.text)
                    time.sleep(2)
                    self.crack()

            mspan = self.browser.find_elements_by_class_name('gt_info_type')
            if len(mspan) > 0:
                info = mspan[0].text
                print('info:', info)
                if '验证失败:' in info:
                    time.sleep(2)
                    self.crack()
        except Exception as e:
            print(e)



if __name__ == '__main__':
    crack = Crack('username', 'passwd')
    crack.crack()
    print('验证成功')