from email import header
import requests
import json
from jsonpath import jsonpath
from aip import AipSpeech
def wehather():
    url = "https://api.seniverse.com/v3/weather/now.json?key=你的心知天气apikey&location=chengdu&language=zh-Hans&unit=c"
    resp = requests.get(url)
    area_name = jsonpath(resp.json(),'$..name')
    arer_temperature = jsonpath(resp.json(),'$..temperature')
    area_code = jsonpath(resp.json(),'$..code')
    area_text = jsonpath(resp.json(),'$..text')
    area_com = [area_name,arer_temperature,area_code,area_text]
    resp.close()
    return area_com


def state():
    url = "https://v1.hitokoto.cn/?c=f&encode=text"
    resp = requests.get(url)
    return resp.text


def history_day(i):
    url = "https://api.iyk0.com/lishi/"
    resp = requests.get(url)
    year = jsonpath(resp.json(),'$..year')
    happend = jsonpath(resp.json(),'$..title')
    p = len(year)
    if(i == p):
        i = 0
    just_first = year[i] + happend[i]
    return just_first

def now_day():


    url = "https://api.muxiaoguo.cn/api/yinlongli?api_key=7bb8aec6dbcf6a04"
    resp = requests.get(url)
    gregorian = jsonpath(resp.json(),'$..gregorian')
    lunar = jsonpath(resp.json(),'$..lunar')
    temporal = jsonpath(resp.json(),'$..temporal')
    lunarYearName = jsonpath(resp.json(),'$..lunarYearName')
    time_source = [gregorian,lunar,temporal,lunarYearName]
    resp.close()
    return time_source

def autop(text0):
    """ 你的 APPID AK SK """
    APP_ID = '百度智能云'
    API_KEY = '百度智能云'
    SECRET_KEY = '百度智能云'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result  = client.synthesis(f'{text0}', 'zh', 1, {
        'vol': 15,
        'per':4
    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('/home/pi/Desktop/dd/audio.mp3', 'wb') as f:
            f.write(result)



def img():
    url = "https://api.ixiaowai.cn/api/api.php"
    resp = requests.get(url)
    f = open("/home/pi/Desktop/dd/bg.png",'wb+')
    f.write(resp.content)

def terminal():
    url = "http://192.168.31.136/LED"
    resp = requests.post(url)
