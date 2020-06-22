import re
import json
import urllib
import requests
def get_value(text):
    '''
    请求百度AI DNN语言模型，判断语句的通顺度
    '''
    url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=xxxxx&client_secret=xxxx'
    res = eval(requests.get(url).text)
    assess_token = res['access_token']
    url = 'https://aip.baidubce.com/rpc/2.0/nlp/v2/dnnlm_cn?access_token=' + str(assess_token)
    data = {"text":text}
    data=json.dumps(data).encode('GBK')
    request = urllib.request.Request(url, data)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request).read()
    result = str(response, encoding="gbk")
    filter_str = re.compile('ppl": (.*)')
    value = re.findall(filter_str,str(response))
    return float(str(value)[2:-4])
