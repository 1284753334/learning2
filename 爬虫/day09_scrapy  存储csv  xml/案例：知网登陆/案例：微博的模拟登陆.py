#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG

from selenium import webdriver
import time



from selenium import webdriver
import pytesseract
from PIL import Image
import time
from chaojiying import Chaojiying
from io import BytesIO


loginname = '18790579029'
password = 'Hph6927962318'
# loginname = '3414018462@qq.com'
# password = 'qikuedu9527'
CHAOJIYING_USERNAME = '18790579029'
CHAOJIYING_PASSWORD = '6927962318'
# CHAOJIYING_SOFT_ID = '1bce712d583f72be3a40d5960a86c94f'
CHAOJIYING_SOFT_ID = 'c77b1ef30e92bf4895d6a180c32ad654'
CHAOJIYING_KIND = 1005

def login():
    '''
    微博的登陆
    :return:
    '''
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        # 加载登录页面
        url = 'http://www.weibo.com/login.php'
        driver.get(url)
        time.sleep(2)
        print('输入用户名...')
        elem_user = driver.find_element_by_id("loginname")
        elem_user.clear()
        elem_user.send_keys(loginname)
        time.sleep(2)
        print('输入密码...')
        elem_pwd =driver.find_element_by_name("password")
        elem_pwd.clear()
        elem_pwd.send_keys(password)
        time.sleep(3)
        checkCode=driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/div/input')
        driver.save_screenshot('./images/weibo.png')
        img = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/a/img')
        left = img.location['x']  # 验证码图片左上角横坐标
        top = img.location['y']  # 验证码图片左上角纵坐标
        right = left + img.size['width']  # 验证码图片右下角横坐标
        bottom = top + img.size['height']  # 验证码图片右下角纵坐标
        im = Image.open('./images/weibo.png')
        im_crop = im.crop((left, top, right, bottom))  # 这个im_crop就是从整个页面截图中再截出来的验证码的图片
        im_crop.save('./images/zrecaptchar.png')

        chaojiying = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID)
        # 识别验证码
        bytes_array = BytesIO()
        im_crop.save(bytes_array, format='PNG')
        strcode = chaojiying.post_pic(bytes_array.getvalue(), CHAOJIYING_KIND)
        print(strcode)
        print(strcode['pic_str'])

        checkCode.send_keys(strcode['pic_str'])

        print('登陆微博...')
        '//*[@id="pl_login_form"]/div/div[3]/div[6]/a'
        login_btn = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a')
        login_btn.click()
        print('已经点击')
        time.sleep(10)
        print(driver.current_url)
        driver.quit()
    except Exception as e:
        print('login error.')


if __name__ == '__main__':
    login()




