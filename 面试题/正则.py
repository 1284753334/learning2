
from lxml import etree
html2 = '''<td class="ip"><p style="display:none;"></p><span></span><span style="display:inline-block;">18</span><span style="display:inline-block;"></span><p style="display:none;">2</p><span>2</span><div style="display:inline-block;">.3</div><p style="display:none;"></p><span></span><div style="display:inline-block;"></div><p style="display:none;">4</p><span>4</span><span style="display:inline-block;">.</span><span style="display:inline-block;">10</span><div style="display:inline-block;"></div><p style="display:none;">3</p><span>3</span><span style="display:inline-block;">.</span><span style="display:inline-block;"></span><p style="display:none;"></p><span></span><div style="display:inline-block;">1</div><p style="display:none;">69</p><span>69</span>:<span class="port HZZZC">9999</span></td>

'''
html1 = '''<a class="ip">12345</a><p>123</p>'''
import re
pat = re.compile(r'(<.*>(.*)</.*>).*',re.M | re.S)
obj = pat.findall(html2)
print(obj)

# html = etree.parse(html1)

# data = html.xpath('td[@class="ip"]')
# info = data.xpath('string(.)').extract()[0]
# print(info)





