import urllib
import http.cookiejar
import ssl
import requests
import json
print('hahah')

def addAiticle(pgc_id):
    headers = {
        'POST http':'https://mp.toutiao.com/mp/agw/article/publish?source=mp&type=article&_signature=_02B4Z6wo00101ezsKwAAAIBAoaL5WxThnfns6C-AACRcDWArbTVffuxdPskFxQdLBKFMwpMwwteivNm32Z.HpYGR-2q1ic4DLE3atRjCpY8xDlrolxvutRfLZ4KVProTo1NDllLULbPaV4wk3f HTTP/1.1',
        'Host':'mp.toutiao.com',
        'Connection':'keep-alive',
        'Content-Length':'733',
        'Originv':'https://mp.toutiao.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
        'Accept':'application/json, text/plain, */*',
        'Referer':'https://mp.toutiao.com/profile_v4/graphic/publish',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
        'Cookie':'tt_webid=6873270729850045959; _'\
            'ba=BA0.2-20200917-5110e-kuOQloX4jZT0fEuvTtxZ; '\
            's_v_web_id=verify_kf6675pk_ZMlIVQDW_WSBx_4fZF_AvIh_jYs3akCokbDr; '\
            'passport_csrf_token=4fe3a0e34a8bf0d8f3f2dc8600a53f22; '\
            'sso_auth_status=aac9a1fd4ca0f3a5d3afa836eb237d32; '\
            'sso_uid_tt=174408113135cf39707f58174745a275; '\
            'sso_uid_tt_ss=174408113135cf39707f58174745a275; '\
            'toutiao_sso_user=d4211b95b5a3d89f8ada2b88867f37a8; '\
            'toutiao_sso_user_ss=d4211b95b5a3d89f8ada2b88867f37a8; '\
            'passport_auth_status=233765f666995ca8ee4f0267c0e7d1b2%2C54672c9fb8ec4460ee5063b718f9aa96; '\
            'sid_guard=d4ca138a4a7af80601ebddc44cf28868%7C1600308246%7C5184000%7CMon%2C+16-Nov-2020+02%3A04%3A06+GMT; '\
            'uid_tt_ss=04134dc53d1c47123ae16f2a178d4df2; sid_tt=d4ca138a4a7af80601ebddc44cf28868; '\
            'sessionid=d4ca138a4a7af80601ebddc44cf28868; sessionid_ss=d4ca138a4a7af80601ebddc44cf28868; '\
            'gftoken=ZDRjYTEzOGE0YXwxNjAwMzA4MjQ2ODZ8fDAGBgYGBgY; uid_tt=04134dc53d1c47123ae16f2a178d4df2c9cd067647acc241c0c48b1d364c3ed5; '\
            'ttcid=96fe79af40254fe885bdd250d009a6d140; MONITOR_WEB_ID=48fcd570-0153-4551-8ca4-9aa374642708; tt_scid=bfUDV3tpH8QKLMl3FOn2075tWuHbleWX7VIF65clMxy3EdYFDblYxd3IAESFGAji2300'}#\

#'pgc_id=6873288350631985667&source=0&content=%3Cp%3E2e%3C%2Fp%3E&title=11111&search_creation_info=%7B%22abstract%22%3A%22%22%7D&title_id=1600311678909_1678044895007756&extra=%7B%22content_word_cnt%22%3A2%2C%22gd_ext%22%3A%7B%22entrance%22%3A%22hotspots%22%2C%22from_page%22%3A%22publisher_mp%22%2C%22enter_from%22%3A%22PC%22%2C%22device_platform%22%3A%22mp%22%2C%22is_message%22%3A0%7D%7D&mp_editor_stat=%7B%7D&educluecard=&draft_form_data=%7B%22coverType%22%3A2%7D&pgc_feed_covers=%5B%5D&claim_origin=0&origin_debut_check_pgc_normal=0&is_fans_article=0&govern_forward=0&praise=0&disable_praise=0&extern_link=&article_ad_type=2&tree_plan_article=0&activity_tag=0&trends_writing_tag=0&community_sync=0&save=0&timer_status=0&timer_time='}
    data = {'pgc_id': pgc_id,
            'source':'0',
            'content':'<p>666666666</p>',
            'title':'777777',
            'search_creation_info':'{"abstract":""}',
            'title_id':'1600311678909_1678044895007759',
            'extra':'{"content_word_cnt":2,"gd_ext":{"entrance":"hotspots","from_page":"publisher_mp","enter_from":"PC","device_platform":"mp","is_message":0}}',
            'mp_editor_stat':'{}',
            'educluecard':'0',
            'draft_form_data':'{"coverType":2}',
            'pgc_feed_covers':'[]',
            'claim_origin':'0',
            'origin_debut_check_pgc_normal':'0',
            'is_fans_article':'0',
            'govern_forward':'0',
            'praise':'0',
            'disable_praise':'0',
            'extern_link':'',
            'article_ad_type':'0',
            'tree_plan_article':'0',
            'activity_tag':'0',
            'trends_writing_tag':'0',
            'community_sync':'0',
            'save':'0',
            'timer_status':'0',
            'timer_time':'',
            }
    r = requests.post('https://mp.toutiao.com/mp/agw/article/publish?source=mp&type=article&_signature=_02B4Z6wo00101ezsKwAAAIBAoaL5WxThnfns6C-AACRcDWArbTVffuxdPskFxQdLBKFMwpMwwteivNm32Z.HpYGR-2q1ic4DLE3atRjCpY8xDlrolxvutRfLZ4KVProTo1NDllLULbPaV4wk3f', data=data, headers=headers)
    print(r.text)

addAiticle('6873288350631985630')