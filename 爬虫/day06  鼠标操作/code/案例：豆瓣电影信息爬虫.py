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

import requests
import time
import random


def load_movie_page(page):
    print('page:',page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    try:
        url = 'https://movie.douban.com/j/new_search_subjects'
        params = {
            'sort': 'U',
            'range': '0,10',
            'tags': '电影',
            'start': (page-1)*20,
            'genres': '喜剧',
            'countries': '中国大陆',
            'year_range': '2018,2018',
        }
        response = requests.get(url,params=params,headers=headers)
        data = response.json()['data']
        print('len:',len(data))
        for item in data:
            print('casts:',item['casts'])
            print('cover:',item['cover']) #
            print('directors:',item['directors'])
            print('id:',item['id'])
            print('rate:',item['rate'])
            print('star:',item['star'])
            print('title:',item['title'])
            print('url:',item['url'])
            print('='*200)
    except Exception as e:
        print('error...')

if __name__ == '__main__':
    for i in range(1,5):
        load_movie_page(i)
        time.sleep(random.random())
