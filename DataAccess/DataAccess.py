import requests
from bs4 import BeautifulSoup

#国家疾控中心新型冠状病毒感染的肺炎疫情分布网站
url = 'http://2019ncov.chinacdc.cn/2019-nCoV/'
r = requests.get(url)
#print(r.status_code)
#print(r.encoding)
#print(r.headers)

r.encoding = 'utf-8'
text = r.text
#print(text)
soup = BeautifulSoup(text, 'lxml')
#print(soup.prettify())

#从上面发现了一个静态地址,其他效果都是JavaScript脚本动态渲染的结果
url = 'http://2019ncov.chinacdc.cn/2019-ncov/mobile.html'
r = requests.get(url)
#print(r.status_code)
#print(r.encoding)
#print(r.headers)

r.encoding = 'utf-8'
text = r.text
#print(text)
soup = BeautifulSoup(text, 'lxml')
#print(soup.prettify())

#提起全国新增与累计数据
newDate = soup.find('span', attrs={'id': 'newDate'}).get_text()
quezhenNew = soup.find('span', attrs={'id': 'quezhenNew'}).get_text()
yisiNew = soup.find('span', attrs={'id': 'yisiNew'}).get_text()
siwangNew = soup.find('span', attrs={'id': 'siwangNew'}).get_text()
print(newDate, quezhenNew, yisiNew, siwangNew)

otherDate = soup.find('span', attrs={'class': ['otherDate']}).get_text()
quezhenSum = soup.find('span', attrs={'id': 'quezhenSum'}).get_text()
yisiSum = soup.find('span', attrs={'id': 'yisiSum'}).get_text()
siwangSum = soup.find('span', attrs={'id': 'siwangSum'}).get_text()
print(otherDate, quezhenSum, yisiSum, siwangNew)

#提取湖北省新增与累计数据
#print(soup.prettify())
proviceTotal = soup.find('div', attrs={'id': 'proviceTotal'})
print(proviceTotal.prettify())
otherDate = proviceTotal.find('span', attrs={'class': ['otherDate']}).get_text()
print(otherDate)
table = proviceTotal.find_all('div', attrs={'class': ['tablerow']})
print(table)

#结果这里面的内容也是动态生成的，不过好在生成的数据格式是直接的数据表，所以决定接卸这里面的Javacript脚本，最终得到数据。
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Firefox()
driver = webdriver.PhantomJS(executable_path='/home/dkk/phantomjs-2.1.1-linux-x86_64/bin/phantomjs', service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
driver.get(url)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'tablerow')))
soup = BeautifulSoup(driver.page_source, "lxml")
driver.close()

print(soup.prettify())
table = proviceTotal.find_all('div', attrs={'class': ['tablerow']})
print(table)
#到此卡住了，提取动态网页未成功，未完待续