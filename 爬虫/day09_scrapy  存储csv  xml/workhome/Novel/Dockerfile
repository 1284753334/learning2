
# 使用哪个python
FROM python:3.8
#把当前项目的  代码放到虚拟容器的code目录下
ADD . /Novel
# 指定的工作目录  ——————./code
WORKDIR /Novel
#把scrap.conf  拷贝到 指定位置
COPY ./scrapyd.conf /etc/scrapyd/
#端口为6800
EXPOSE 6800
# 在容器里安装这些类库
RUN pip3 install -r requirements.txt
CMD scrapyd

