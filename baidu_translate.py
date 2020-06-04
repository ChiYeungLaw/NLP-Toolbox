import http.client
import hashlib
import json
import urllib
import random

# Chinese to English
def baidu_translate_zh2en(content):
    appid = 'xxxxxxx'
    secretKey = 'xxxxxxx'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content
    fromLang = 'zh' # source language
    toLang = 'en'   # target language
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
 
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")
        js = json.loads(jsonResponse)
        dst = str(js["trans_result"][0]["dst"])  # get the translation result
        return dst # return the result
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
