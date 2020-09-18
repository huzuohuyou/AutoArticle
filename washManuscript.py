import urllib
import http.cookiejar
import ssl
import requests
import json


def washAiticle(article):
    headers = {
        'POST http':'http://18.217.155.9/api/open/xi HTTP/1.1',
        'Host':'18.217.155.9',
        'Connection':'keep-alive',
        'Content-Length':'733',
        'Originv':'http://mutou888.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Referer':'http://mutou888.com/projects/guling/index.html',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8'}#\

#'pgc_id=6873288350631985667&source=0&content=%3Cp%3E2e%3C%2Fp%3E&title=11111&search_creation_info=%7B%22abstract%22%3A%22%22%7D&title_id=1600311678909_1678044895007756&extra=%7B%22content_word_cnt%22%3A2%2C%22gd_ext%22%3A%7B%22entrance%22%3A%22hotspots%22%2C%22from_page%22%3A%22publisher_mp%22%2C%22enter_from%22%3A%22PC%22%2C%22device_platform%22%3A%22mp%22%2C%22is_message%22%3A0%7D%7D&mp_editor_stat=%7B%7D&educluecard=&draft_form_data=%7B%22coverType%22%3A2%7D&pgc_feed_covers=%5B%5D&claim_origin=0&origin_debut_check_pgc_normal=0&is_fans_article=0&govern_forward=0&praise=0&disable_praise=0&extern_link=&article_ad_type=2&tree_plan_article=0&activity_tag=0&trends_writing_tag=0&community_sync=0&save=0&timer_status=0&timer_time='}
    data = {'content': article,}
    r = requests.post('http://18.217.155.9/api/open/xi', data=data, headers=headers)
    return r.text

json_str = washAiticle('6873288350631985630')
data = json.loads(json_str)
print(data['msg'])