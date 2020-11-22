import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chaojiying import Chaojiying

EMAIL = 'guojiantao@163.com'
PASSWORD = '123456'

CHAOJIYING_USERNAME = 'Thompson'
CHAOJIYING_PASSWORD = 'Thompson'
CHAOJIYING_SOFT_ID = '1bce712d583f72be3a40d5960a86c94f'
CHAOJIYING_KIND = 9004


class CrackTouClick():
    def __init__(self):
        self.url = 'https://kyfw.12306.cn/otn/login/init'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD
        self.chaojiying = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID)
    
    # def __del__(self):
    #     self.browser.close()

    
    def crack(self):
        """
        破解入口
        :return: None
        """
        self.browser.get(self.url)
        #print(self.browser.page_source)
        email = self.wait.until(EC.presence_of_element_located((By.ID, 'username')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        email.send_keys(self.email)
        password.send_keys(self.password)

        time.sleep(2)
        # 点击验证码刷新按钮 element_to_be_clickable
        button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'touclick-reload')))
        # 点击验证码刷新按钮
        button.click()
        time.sleep(2)
        # 获取验证码图片
        # 获取验证码元素位置范围
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'touclick-image')))
        time.sleep(2)
        location = element.location
        size = element.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        print('验证码位置', top, bottom, left, right)
        # 网页快照  全屏
        self.browser.save_screenshot("./images/12306.png")
        screenshot = Image.open("./images/12306.png")
        #screenshot = self.browser.get_screenshot_as_png()
        #screenshot = Image.open(BytesIO(screenshot))
        # 截取验证码图片  小片
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save("./images/captcha.png")

        bytes_array = BytesIO()
        captcha.save(bytes_array, format='PNG')
        # 识别验证码
        result = self.chaojiying.post_pic(bytes_array.getvalue(), CHAOJIYING_KIND)
        print(result)
        # 解析识别结果
        groups = result.get('pic_str').split('|')
        locations = [[int(number) for number in group.split(',')] for group in groups]
        # 点击验证图片
        for location in locations:
            print(location)
            element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'touclick-image')))
            ActionChains(self.browser).move_to_element_with_offset(element, location[0],location[1]).click().perform()
            time.sleep(1)
        # 点击确定按钮
        # button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn200s')))
        # button.click()
        # # 判定是否成功error_msgmypasscode1
        # try:
        #     elem = self.wait.until(
        #          EC.visibility_of_element_located((By.CLASS_NAME, 'error')))
        #     print(elem)
        # except Exception as e:
        #     print(e)
        #     self.login()
        
        #失败后重试
        # if not success:
        #     self.crack()
        # else:
        #     self.login()


if __name__ == '__main__':
    crack = CrackTouClick()
    crack.crack()
