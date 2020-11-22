# # import requests
# #
# # # url = 'https://www.zhipin.com/job_detail/?query=java&city=101210100&industry=&position='
# # url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
# # headers = {
# # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
# # }
# # response = requests.get(url,headers=headers).text
# # print(response)
#
#
#
#
#
# #
# #用于请求网页数据
# import requests
# #正则表达式、json字典
# import re,json
# #爬取过程中用于暂停
# import time
# #用于操作Excel
# import openpyxl
# #模拟真实用户获取职位信息总页数
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# #使用bs4解析网页
# from bs4 import BeautifulSoup as bs
#
# # #预调用selenium
# # chrome_options = Options()
# # # chrome_options.add_argument('--headless')
# # chrome_options.add_argument('--disable-gpu')
#
# #大致的url框架
# url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%s,2,%s.html'
# #请求头
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36'
#     }
# #要爬取的职位关键词
# keyword = input('请输入您想要抓取的职位信息关键词：')
# #创建工作表
# wb = openpyxl.Workbook()
# ws = wb.active
# ws.title = "前程无忧%s工作信息" % keyword
# print('45432345')
#
#
# """
# 因为总页数调用了js文件
# 用requests的话返回的数据里找不到
# 所以使用selenium获取职位信息总页数
# 嫌麻烦的话可以直接去前程无忧网站搜索一下关键词...
# """
# def get_page():
#     #访问第一页即可
#     URL = url % (keyword,str(1))
#     #selenium无可视化
#     # browser = webdriver.Chrome(executable_path = 'chromedriver.exe',options = chrome_options)
#     # browser = webdriver.Chrome(options = chrome_options)
#     #访问网页
#     # browser.get(URL)
#     #保存网页数据
#     # page_text = browser.page_source
#     page_text = requests.get(URL,headers=headers).text
#     # print(page_text)
#     #正则匹配，括号内是要返回的信息 关键字是 如何找到的
#     pattern = re.compile('"total_page":"(.*?)"')
#     #匹配所有信息，并获取列表头，实际上也就只有一条
#     number = re.findall(pattern,page_text)[0]
#     return number
#
#
# #清洗工资数据，这里借用了大佬的方法
# def wish_data(wages_old):
#     if '元/天' in wages_old:
#         if '-' in wages_old.split('元')[0].split('-')[0]:
#             wages1 = wages_old.split('元')[0].split('-')[1]
#             wages2 = wages_old.split('元').split('-')[1]
#             wages_new = (float(wages2) + float(wages1)) / 2 * 30
#         else:
#             wages_new = float(wages_old.split('元')[0]) * 30
#         return wages_new
#     elif '千/月' in wages_old or '千以下/月' in wages_old or '千以上/月' in wages_old:
#         if '-' in wages_old.split('千')[0]:
#             wages1 = wages_old.split('千')[0].split('-')[0]
#             wages2 = wages_old.split('千')[0].split('-')[1]
#             wages_new = (float(wages2) + float(wages1)) / 2 * 1000
#         else:
#             wages_new = float(wages_old.split('千')[0]) * 1000
#         return wages_new
#     elif '万/月' in wages_old or '万以下/月' in wages_old or '万以上/月' in wages_old:
#         if '-' in wages_old.split('万')[0]:
#             wages1 = wages_old.split('万')[0].split('-')[0]
#             wages2 = wages_old.split('万')[0].split('-')[1]
#             wages_new = (float(wages2) + float(wages1)) / 2 * 10000
#         else:
#             wages_new = float(wages_old.split('万')[0]) * 10000
#         return wages_new
#     elif '万/年' in wages_old or '万以下/年' in wages_old or '万以上/年' in wages_old:
#         if '-' in wages_old.split('万')[0]:
#             wages1 = wages_old.split('万')[0].split('-')[0]
#             wages2 = wages_old.split('万')[0].split('-')[1]
#             wages_new = (float(wages2) + float(wages1)) / 2 * 10000 / 12
#         else:
#             wages_new = float(wages_old.split('千')[0]) * 10000 / 12
#     #小数部分四舍五入并返回清洗后的数据
#     return round(wages_new)
#
#
# #获取每一页中的职位信息
# def get_dict(i):
#     #使用requests访问网页
#     response = requests.get(url = url % (keyword,str(i)),headers = headers)
#     #设定数据的格式
#     response.encoding = response.apparent_encoding
#     print('type:',response.encoding)
#     #保存网页数据
#     html = response.text
#     #其实这里使用bs4仅仅是解决Unicode编码问题
#     bf = bs(html,'lxml')
#     #第一次正则匹配，匹配所有的职位信息
#     pattern_string = re.compile('window.__SEARCH_RESULT__\s=\s(.*?),"jobid_count"')
#
#     # data = re.findall(pattern_string,str(bf))
#     data = re.findall(pattern_string,html)
#     print('data:',data)
#     for i in data:
#         print('i:',i)
#     #删除信息中所有的转义字符
#     data = data[0].replace('\\','')
#     #第二次正则匹配，逐条划分职位信息
#     pattern_getlist = re.compile('{"type".*?}')
#     #注意此时获取的是一个列表而不是字典
#     dict1 = re.findall(pattern_getlist,data)
#     return dict1
#
#
# #将职位信息逐条添加到工作表中
# def save_data(data_dict):
#     #获取列表长度，其实可以直接用for i in range(len(data_dict))
#     length = len(data_dict)
#     for i in range(length):
#         #将信息加载为字典
#         dict2 = json.loads(data_dict[i])
#         #捕捉一些保存在字典中列表的数据
#         content = dict2['attribute_text']
#         #学历要求
#         education = ''.join([i for i in content if i in '本科大专应届生在校生硕士'])
#         #招聘人数
#         need_people = ''.join([i for i in content if '招' in i])
#         #英语要求，似乎都没有写明...也可能写的是四六级叭
#         english = ''.join([i for i in content if '英语' in i])
#         #如果经历要求为空的话则设置为不详
#         if dict2['workyear'] == '':
#             dict2['workyear'] = '不详'
#         #否则为其加个‘年’字
#         else:
#             dict2['workyear'] += '年'
#         #如果公司福利为空的话则设置为不详
#         if dict2['jobwelf'] == '':
#             dict2['jobwelf'] = '不详'
#         #如果工资没有写明的话设置为面议
#         if dict2['providesalary_text'] == '':
#             dict2['providesalary_text'] = '面议'
#         #如果写明的话则调用函数对数据进行清洗
#         #不想清洗的话将else语句注释掉即可，我这里是为了绘图方便
#         else:
#             dict2['providesalary_text'] = wish_data(dict2['providesalary_text'])
#         #以下两项同理，没有匹配到也设置为不详
#         if education == '':
#             education += '不详'
#         if english == '':
#             english += '不详'
#         #为工作表添加一行数据
#         ws.append([
#             dict2['job_title'],
#             dict2['workarea_text'],
#             dict2['providesalary_text'],
#             education,
#             dict2['workyear'],
#             need_people,
#             #这里只取发布的日期，空格作为分隔符
#             dict2['issuedate'].split(' ')[0],
#             english,
#             dict2['job_href'],
#             dict2['company_name'],
#             dict2['companyind_text'],
#             dict2['companysize_text'],
#             dict2['jobwelf'],
#             dict2['company_href']
#             ])
#
#
# def run():
#     #工作表的第一行，设置各列标题
#     ws.append(['职位','地区','月薪(元)','学历要求','经验要求','招聘人数','发布时间','英语要求',
#                '职位详情','公司信息','公司行业','公司规模','福利待遇','公司详情'])
#     #调整工作表的列宽
#     for column in ['A','I','J','K','M','N']:
#         ws.column_dimensions[column].width = 22.0
#     for column in ['B','G']:
#         ws.column_dimensions[column].width = 13.0
#     #获取页数并转化为整数型变量
#     n = int(get_page())
#     print("%s职位共有%s页" % (keyword,str(n)))
#     #按需爬取
#     need_page = int(input('请输入您想要抓取的页数：'))
#     #用于大量网页出现异常时结束循环
#     error_page = 0
#     #统计爬取出错的页数
#     error_list = []
#     #开始循环爬取每一页，将n修改为具体数值以限定要爬取的总页数
#     for i in range(1,need_page + 1):
#         #捕捉异常，如有异常则爬取下一页
#         try:
#             data_dict = get_dict(i)
#             save_data(data_dict)
#             #提示抓取成功
#             print("第%s页数据抓取完成！" % str(i))
#         except:
#             #遇到异常时将错误页数增加1
#             error_page += 1
#             #将错误页添加到统计列表
#             error_list.append(i)
#             #提示错误
#             print("第%s页：error" % str(i))
#             pass
#         #当总的错误页数大于20时，退出循环，可以自行设定退出条件
#         if error_page > 20:
#             print("出现了不可控的异常！已经退出循环！")
#             break
#         #将程序休眠3秒，防止爬取速度过快被封IP地址
#         #也是因为这个原因，所以没有使用多线程，其实是不会2333
#         time.sleep(3)
#     #当错误页数不为0的时候，输出统计到的错误页列表
#     if error_page != 0:
#         print('以下页数抓取失败：')
#         print(error_list)
#     #提示程序执行完成
#     print("所有数据抓取完成！")
#     """
#     将工作表保存，如果中途结束则什么都没有
#     所以事先想好要爬的页数
#     或者按需要修改成每爬取一页就保存一次
#     具体怎么做就不再详述了
#     """
#     wb.save('前程无忧%s职位信息.xlsx' % keyword)
#     print('1234')
#
#
#
# #入口函数
# if __name__ == '__main__':
#     run()
#     # get_page()
#
#     # def get_data():
#     #     #读取工作表的第2、3、4列
#     #     filename = '前程无忧python职位信息.xlsx'
#     #     df = pd.read_excel(filename, usecols= [2,3,4])
#     #     #删除空值
#     #     df = df.drop(df[df['月薪(元)'] == '面议'].index)
#     #     df = df.drop(df[df['经验要求'] == '不详'].index)
#     #     df = df.drop(df[df['学历要求'] == '不详'].index)
#     #     #修改列标题
#     #     df.rename(columns={'月薪(元)':'工资','经验要求':'经验','学历要求':'学历' }, inplace=True)
#     #     #需要保存的话就把注释取消掉
#     #     #df.to_excel('绘图数据.xlsx')
#     # #将“工资列”的数据定义位整型
#     #     df['工资'] = df['工资'].astype("int")
#     #     return df
