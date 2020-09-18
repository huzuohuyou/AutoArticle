import urllib
import http.cookiejar
import ssl
import requests
import json
from bs4 import BeautifulSoup
import re
def getTop():
    headers = {
        'GET http':'GET https://s.weibo.com/top/summary HTTP/1.1',
        'Host':'s.weibo.com',
        'Connection':'keep-alive',
        'Cache-Control':'max-age=0',
        'Upgrade-Insecure-Requests': '1',
       
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
        'Cookie':'SUB=_2AkMoP5sNf8NxqwJRmP4WyWzgaYxxwwvEieKeY2rWJRMxHRl-yT9kqlwOtRB6A7-14qMstznOFVQf1tWbQIntCHu-b6od; '\
            'SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFYO55bTOpgTxd_.kO2nqv7; '\
            'login_sid_t=917b7c12569c8159aeaf9ecd08e769c4; '\
            'cross_origin_proto=SSL; _'\
            's_tentry=passport.weibo.com; '\
            'Apache=6260817897682.08.1600328772874; '\
            'SINAGLOBAL=6260817897682.08.1600328772874; '\
            'ULV=1600328772888:1:1:1:6260817897682.08.1600328772874:; '\
            'UOR=,,www.baidu.com; '\
            'WBtopGlobal_register_version=434eed67f50005bd'}

    data = { }
    res = requests.get('https://s.weibo.com/top/summary', data=data, headers=headers)
    # print(res.text)
    html = res.text
    soup = BeautifulSoup(html,'html.parser')
    # print(soup) 
    items = soup.find_all('a',href=re.compile("weibo"))
    for item in items:
        print(item.text)
getTop()